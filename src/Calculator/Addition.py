from src.Calculator.ValidateException import exceptions


def addition(a, b):
    err = exceptions(a, b)
    if err:
        return int(a) + int(b)
    else:
        return 0
