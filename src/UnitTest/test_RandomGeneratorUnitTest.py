import unittest
from pprint import pprint
from src.RandomGenerator.RandomGen import Random


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.random = Random()
        self.start = 1
        self.end = 100
        self.length = 6
        self.seed = 5
        self.num_val = 3
        # self.list = self.random.random_integer_list(self.start, self.end, self.length, self.seed)

    def test_instantiate_calculator_self(self):
        self.assertIsInstance(self.random, Random)


    def test_random_without_seed_integer(self):
        int_random = self.random.random_without_seed_integer(self.start, self.end)
        pprint(int_random)
        self.assertEqual(isinstance(self.random.random_without_seed_integer(self.start, self.end), int), True)

    def test_random_without_seed_decimal(self):
        decimal_random = self.random.random_without_seed_decimal(self.start, self.end)
        pprint(decimal_random)
        self.assertEqual(isinstance(self.random.random_without_seed_decimal(self.start, self.end), float), True)

    def test_random_with_seed_integer(self):
        int_rd_seed = self.random.random_with_seed_integer(self.start, self.end, self.seed)
        self.assertEqual(self.random.random_with_seed_integer(self.start, self.end, self.seed), int_rd_seed)
