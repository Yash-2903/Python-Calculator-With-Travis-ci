from src.Calculator.Addition import addition
from src.Calculator.Division import division


def mean(data):
    try:
        total_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(total_values, total)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("ERROR!  That is an empty array.  Try again")
