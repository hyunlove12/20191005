from calculator.model import CalculatorModel
import os
if __name__ == '__main__':
    calc = CalculatorModel()
    calc.create_div_model()
    #리눅스에서 돌아간다
    #모델이 존재하지 않을경우만 실행한다.
    #모델을 공유하여 생성하기떄문에 같이 실행하면 뒤에 모델은 추가되어 생성되기 때문에 오륩라생
    #if not os.path.exists('saved_add_model/checkpoint'):
    #    calc.create_add_model()
    #if not os.path.exists('saved_min_model/checkpoint'):
    #    calc.create_min_model()
    #if not os.path.exists('saved_mul_model/checkpoint'):
    #    calc.create_mul_model()
    #if not os.path.exists('saved_div_model/checkpoint'):
    #    calc.create_div_model()
