from src.RandomGenerator.RandomGenWithoutSeedDecimal import random_without_seed_decimal
from src.RandomGenerator.RandomGenWithoutSeedInteger import random_without_seed_integer
from src.RandomGenerator.RandomGenWithSeedDecimal import random_with_seed_decimal
from src.RandomGenerator.RandomGenWithSeedInteger import random_with_seed_integer
from src.RandomGenerator.RandomGenWithSeedListInteger import random_with_seed_list_integer
from src.RandomGenerator.RandomGenWithSeedListDecimal import random_with_seed_list_decimal


class Random:
    result = 0


    def random_without_seed_decimal(self, start, end):
        self.result = random_without_seed_decimal(start, end)
        return self.result


    def random_without_seed_integer(self, start, end):
        self.result = random_without_seed_integer(start, end)
        return self.result


    def random_with_seed_decimal(self, start, end, seed):
        self.result = random_with_seed_decimal(start, end, seed)
        return self.result


    def random_with_seed_integer(self, start, end, seed):
        self.result = random_with_seed_integer(start, end, seed)
        return self.result

    def random_with_seed_list_decimal(self, start, end, length, seed):
        self.result = random_with_seed_list_decimal(start, end, length, seed)
        return self.result

    def random_with_seed_list_integer(self, start, end, length, seed):
        self.result = random_with_seed_list_integer(start, end, length, seed)
        return self.result
