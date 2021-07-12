from src.Calculator.Addition import addition
from src.Calculator.Subtraction import subtraction
from src.Calculator.Division import division


def median(data):
    try:
        total = len(data)
        data.sort()
        if total % 2 == 0:
            median1 = data[int(division(2, total))]
            median2 = data[int(subtraction(division(2, total)), 1)]
            result = division(2, addition(median1, median2))
        else:
            result = data[int(division(2, total))]

        return result
    except ValueError:
        print("ERROR!  Data is Empty.  Try again.")
