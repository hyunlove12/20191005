from calculator.model import CalculatorModel

class CalculatorController:
    def __init__(self, num1, num2, op):
        self.op = op
        self.calc = CalculatorModel(num1, num2)

    def execute(self):
        if self.op == '+':
            result = self.calc.add()
        elif self.op == '-':
            result = self.calc.sub()
        elif self.op == '*':
            result = self.calc.mul()
        elif self.op == '/':
            result = self.calc.div()
        return result
