from numpy import random
from src.RandomGenerator.RandomGenWithoutSeedInteger import random_without_seed_integer


def random_with_seed_integer(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rd_with_seed_integer = random_without_seed_integer(start, end)
        return rd_with_seed_integer
    finally:
        random.set_state(state)
