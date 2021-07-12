from src.Calculator.SquareRoot import squareRoot
from src.Statistics.Variance import variance


def standardDeviation(data):
    try:
        variance_of_data = variance(data)
        return squareRoot(variance_of_data)

    except ValueError:
        print("ERROR!  That is an empty array.  Try again.")