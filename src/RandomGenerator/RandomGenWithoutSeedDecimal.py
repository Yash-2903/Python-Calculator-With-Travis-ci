from numpy.random import uniform


def random_without_seed_decimal(start, end):
    rand = uniform(start, end)
    # round up upto two decimal place digit
    rounded_decimal = round(rand, 2)
    return rounded_decimal
