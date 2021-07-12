from src.Calculator.MainCalculator import MainCalculator
from src.Statistics.Mean import mean
from src.Statistics.Mode import mode
from src.Statistics.Median import median
from src.Statistics.Variance import variance
from src.Statistics.StandardDeviation import standardDeviation


class Statistics(MainCalculator):
    data = []


    def __init__(self):
        super().__init__()


    def mean(self, data):
        self.result = mean(data)
        return self.result


    def median(self, data):
        self.result = median(data)
        return self.result


    def mode(self, data):
        self.result = mode(data)
        return self.result


    def variance(self, data):
        self.result = variance(data)
        return self.result


    def standard_deviation(self, data):
        self.result = standardDeviation(data)
        return self.result
