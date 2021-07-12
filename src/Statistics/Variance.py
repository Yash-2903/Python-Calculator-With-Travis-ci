from src.Calculator.Square import square
from src.Calculator.Division import division
from src.Statistics.Mean import mean


def variance(data):
    try:
        mean_of_data = mean(data)
        total = len(data)
        var = 0
        for i in data:
            var = var + square(i - mean_of_data)
        result = division(total, var)
        return result

    except ValueError:
        print("ERROR: That is an emtpy array! Try again.")