from src.Calculator.MainCalculator import MainCalculator
from src.Statistics.Mean import mean
from src.CSVReader.CSVReader import CSVReader


class Statistics(MainCalculator):
    data = []


    def __init__(self):
        super().__init__()


    def mean(self, data):
        self.result = mean(data)
        return self.result

