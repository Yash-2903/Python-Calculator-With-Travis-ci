from src.RandomGenerator.RandomGenWithoutSeedDecimal import random_without_seed_decimal
from src.RandomGenerator.RandomGenWithoutSeedInteger import random_without_seed_integer


class Random:
    result = 0

    def random_decimal(self, start, end):
        self.result = random_without_seed_decimal(start, end)
        return self.result

    def random_integer(self, start, end):
        self.result = random_without_seed_integer(start, end)
        return self.result
