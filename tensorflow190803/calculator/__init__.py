from calculator.controller import CalculatorController
#패키지  + 클래스
'''
if __name__ == '__main__':
    num1 = int(input('첫번째 수 \n'))
    calc = CalculatorModel(2,3)
    result = calc.add(int(num1),6)
    print('계산결과 %d' % result)
'''
if __name__ == '__main__':
    num1 = int(input('숫자를  입력하세요 \n'))
    num2 = int(input('숫자를  입력하세요 \n'))
    op = input('연산자를 입력하세요 \n')
    calc = CalculatorController(num1, num2, op)
    result = calc.execute()
    print('결과 : %d' %result)

