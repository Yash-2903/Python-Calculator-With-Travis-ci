from src.Calculator.ValidateException import exception


def squareRoot(a):
    err = exception(a)
    if err:
        return int(a) ** (1 / 2)
    else:
        return 0
