from src.Calculator.ValidateException import exception


def square(a):
    err = exception(a)
    if err:
        return int(a) * int(a)
    else:
        return 0
