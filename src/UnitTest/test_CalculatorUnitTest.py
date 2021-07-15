import unittest
from src.Calculator.MainCalculator import MainCalculator
from src.CSVReader.CSVReader import CSVReader
from src.StaticProperties.StaticVariable import StaticVariable
from pprint import pprint


class MyUnitTest(unittest.TestCase):

    def setUp(self) -> None:
        self.mainCalculator = MainCalculator()

    def test_instantiate_calculator(self):
        pprint("Initial Arithmetic")
        self.assertIsInstance(self.mainCalculator, MainCalculator)

    # Unit Test for Addition
    def test_addition(self):
        test_add_data = CSVReader(StaticVariable.unitTestAddition).data
        pprint("Addition Test")
        for row in test_add_data:
            self.assertEqual(self.mainCalculator.add(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.mainCalculator.result, int(row[StaticVariable.result]))

    # Unit Test for Subtraction
    def test_subtraction(self):
        pprint("Subtraction Test")
        test_sub_data = CSVReader(StaticVariable.unitTestSubtraction).data
        for row in test_sub_data:
            self.assertEqual(self.mainCalculator.sub(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.mainCalculator.result, int(row[StaticVariable.result]))

    # Unit Test for Multiplication
    def test_multiplication(self):
        pprint("Multiplication Test")
        test_multiple_data = CSVReader(StaticVariable.unitTestMultiplication).data
        for row in test_multiple_data:
            self.assertEqual(self.mainCalculator.multiple(row[StaticVariable.value1], row[StaticVariable.value2]),
                             int(row[StaticVariable.result]))
            self.assertEqual(self.mainCalculator.result, int(row[StaticVariable.result]))

    # Unit Test for Division
    def test_division(self):
        pprint("Division Test")
        test_div_data = CSVReader(StaticVariable.unitTestDivision).data
        for row in test_div_data:
            self.assertAlmostEqual(self.mainCalculator.div(row[StaticVariable.value1], row[StaticVariable.value2]),
                                   float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.mainCalculator.result, float(row[StaticVariable.result]))

    # Unit Test for Square
    def test_square(self):
        test_sq_data = CSVReader(StaticVariable.unitTestSquare).data
        pprint("Square Test")
        for row in test_sq_data:
            self.assertAlmostEqual(self.mainCalculator.sq(row[StaticVariable.value1]),
                                   float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.mainCalculator.result, float(row[StaticVariable.result]))

    # Unit Test for SquareRoot
    def test_squareRoot(self):
        test_sqrt_data = CSVReader(StaticVariable.unitTestSquareRoot).data
        pprint("SquareRoot Test")
        for row in test_sqrt_data:
            self.assertAlmostEqual(self.mainCalculator.sqrt(row[StaticVariable.value1]),
                                   float(row[StaticVariable.result]))
            self.assertAlmostEqual(self.mainCalculator.result, float(row[StaticVariable.result]))


if __name__ == '__main__':
    unittest.main()
