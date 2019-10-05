class CalculatorModel:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        return result

    def sub(self):
        result = self.num1 - self.num2
        return result

    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        result = self.num1 / self.num2
        return result



