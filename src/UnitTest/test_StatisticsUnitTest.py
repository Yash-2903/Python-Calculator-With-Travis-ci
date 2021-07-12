import unittest
from src.Statistics.Statistics import Statistics
from src.CSVReader.CSVReader import CSVReader
from src.StaticProperties.StaticVariable import StaticVariable


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        self.test_stat_data = CSVReader(StaticVariable.unitTestStatistics).data
        self.testData = [int(row['Value']) for row in self.test_stat_data]


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)


    def test_mean_calculator(self):
        self.assertEqual(self.statistics.mean(self.testData), 6.0)


    def test_mode_calculator(self):
        self.assertEqual(self.statistics.mode(self.testData), [9])


if __name__ == '__main__':
    unittest.main()
