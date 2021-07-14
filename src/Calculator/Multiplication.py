from src.Calculator.ValidateException import exceptions


def multiplication(a, b):
    err = exceptions(a, b)
    if err:
        return int(a) * int(b)
    else:
        return 0
