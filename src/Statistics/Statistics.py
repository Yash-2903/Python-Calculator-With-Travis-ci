from src.Calculator.MainCalculator import MainCalculator
from src.Statistics.Mean import mean
from src.Statistics.Mode import mode
from src.Statistics.Median import median


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


