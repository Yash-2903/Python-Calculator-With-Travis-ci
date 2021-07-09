from Addition import addition
from Subtraction import subtraction
from Multiplication import  multiplication
from Division import division
from Square import square
from SquareRoot import squareRoot


class Calc:
    # Initialization
    result = 0


    def __init__(self):
        pass

    # Addition
    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    # Subtraction
    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    # Multiplication
    def multiple(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    # Division
    def div(self, a, b):
        self.result = division(a, b)
        return self.result

    # Square
    def sq(self, a):
        self.result = square(a)
        return self.result

    # SquareRoot
    def sqrt(self, a):
        self.result = squareRoot(a)
        return self.result
