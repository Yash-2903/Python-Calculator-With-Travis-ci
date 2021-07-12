from numpy.random import uniform


def random_without_seed_decimal(start, end):
    rand = uniform(start, end)
    # rounded to two decimal places
    rounded_decimal = round(2, rand)
    return rounded_decimal
