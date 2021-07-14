from src.Calculator.ValidateException import exceptions


def subtraction(a, b):
    err = exceptions(a, b)
    if err:
        return int(b) - int(a)
    else:
        return 0
