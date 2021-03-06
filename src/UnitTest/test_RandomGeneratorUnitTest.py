import unittest
from pprint import pprint
from src.RandomGenerator.MainRandomGen import Random


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = Random()
        self.start = 1
        self.end = 100
        self.length = 3
        self.seed = 5

    def test_instantiate_calculator_self(self):
        pprint("Initial Random Generator")
        self.assertIsInstance(self.random, Random)


    def test_random_without_seed_integer(self):
        int_random = self.random.random_without_seed_integer(self.start, self.end)
        pprint(int_random)
        pprint("Random Without Seed Integer Test")
        self.assertEqual(isinstance(self.random.random_without_seed_integer(self.start, self.end), int), True)

    def test_random_without_seed_decimal(self):
        decimal_random = self.random.random_without_seed_decimal(self.start, self.end)
        pprint(decimal_random)
        pprint("Random Without Seed Integer Decimal")
        self.assertEqual(isinstance(self.random.random_without_seed_decimal(self.start, self.end), float), True)

    def test_random_with_seed_integer(self):
        pprint("Random With Seed Integer Test")
        int_rd_seed = self.random.random_with_seed_integer(self.start, self.end, self.seed)
        self.assertEqual(self.random.random_with_seed_integer(self.start, self.end, self.seed), int_rd_seed)

    def test_random_with_seed_decimal(self):
        pprint("Random With Seed Decimal Test")
        decimal_rd_seed = self.random.random_with_seed_decimal(self.start, self.end, self.seed)
        self.assertEqual(self.random.random_with_seed_decimal(self.start, self.end, self.seed), decimal_rd_seed)

    def test_random_integer_list(self):
        int_array = self.random.random_with_seed_list_integer(self.start, self.end, self.length, self.seed)
        pprint(int_array)
        pprint("Random With Seed Integer List Test")
        for val in int_array:
            test_value = int(val)
            self.assertEqual(isinstance(test_value, int), True)

    def test_random_decimal_list(self):
        decimal_array = self.random.random_with_seed_list_decimal(self.start, self.end, self.length, self.seed)
        pprint(decimal_array)
        pprint("Random With Seed Decimal List Test")
        for val in decimal_array:
            test_value = float(val)
            self.assertEqual(isinstance(test_value, float), True)
