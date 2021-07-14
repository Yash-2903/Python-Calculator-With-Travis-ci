from src.Calculator.ValidateException import exceptions


def division(a, b):
    try:
        err = exceptions(a, b)
        if err:
            return float(b) / float(a)
        else:
            return 0
    except ZeroDivisionError as error:
        error = "ERROR! you cannot divide by zero!!"
        return error
