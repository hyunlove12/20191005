from flask import Flask
from flask import render_template, request, jsonify
from calculator.controller import CalculatorController
from cabbage.controller import CabbageController
from members.controller import MemberController
import re
app = Flask(__name__)

@app.route("/ui_calc")
def ui_calc():
    stmt = request.args.get('stmt','NONE')
    if(stmt == 'NONE'):
        print('넘어 온 값이 없음')
    else:
        print('넘어온  : {}'.format(stmt))
        #'[0-9]+' -> 0~9까지 한개 이상
        patt = '[0-9]+'
        op = re.sub(patt, '', stmt)
        print('넘어온 연산자:{}'.format(op))
        nums = stmt.split(op)
        result = 0
        n1 = int(nums[0])
        n2 = int(nums[1])
        if op == '+': result = n1 + n2
        elif op == '-': result = n1 - n2
        elif op == '*': result = n1 * n2
        elif op == '/': result = n1 / n2
    return jsonify(result = result)

@app.route('/ai_calc', methods=['post'])
def ai_calc():
    num1 = request.form['num1']
    num2 = request.form['num2']
    opcode = request.form['opcode']
    c = CalculatorController(num1, num2, opcode)
    result = c.calc()
    render_params ={}
    render_params['result'] = int(result)
    print('app.py에 출력 된 덧셈결과 ; {}'.format(result))
    return render_template('ai_calc.html', **render_params)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['post'])
def login():
    userid = request.form['userid']
    password = request.form['password']
    ctrl = MemberController()
#    ctrl.create_table()
    view = ctrl.login(userid, password)
    return render_template(view)


#주소부분을 변수처리
@app.route('/move/<path>')
def move(path):
    return render_template('{}.html'.format(path))

@app.route('/cabbage', methods=['post'])
def cabbage():
    avg_temp = request.form['avg_temp']
    min_temp = request.form['min_temp']
    max_temp = request.form['max_temp']
    rain_fall = request.form['rain_fall']
    ctrl = CabbageController(avg_temp, min_temp, max_temp, rain_fall)
    result = ctrl.service()
    render_params = {}
    render_params['result'] = result
    return render_template('cabbage.html', **render_params)

if __name__ == "__main__":
    app.run()
