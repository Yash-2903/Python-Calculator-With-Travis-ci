import unittest
from src.Statistics.Statistics import Statistics
from src.CSVReader.CSVReader import CSVReader
from src.StaticProperties.StaticVariable import StaticVariable
from numpy import var, std


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.test_stat_data = CSVReader(StaticVariable.unitTestStatistics).data
        self.testData = [int(row[StaticVariable.value]) for row in self.test_stat_data]

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        self.assertEqual(self.statistics.mean(self.testData), StaticVariable.Mean)

    def test_median_calculator(self):
        self.assertEqual(self.statistics.median(self.testData), StaticVariable.Median)

    def test_mode_calculator(self):
        self.assertEqual(self.statistics.mode(self.testData), StaticVariable.Mode)

    def test_variance_method(self):
        varTestValue = (var(self.testData))
        self.assertEqual(self.statistics.variance(self.testData), varTestValue)

    def test_standard_deviation(self):
        stdTestValue = (std(self.testData))
        self.assertAlmostEqual(self.statistics.standard_deviation(self.testData), stdTestValue)


if __name__ == '__main__':
    unittest.main()
