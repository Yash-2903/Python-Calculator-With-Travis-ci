def division(a, b):
    try:
        div = float(b) / float(a)
        return round(div, 9)
    except ZeroDivisionError as error:
        error = "ERROR!  YOU CANNOT DIVIDE BY ZERO!"
        return error
