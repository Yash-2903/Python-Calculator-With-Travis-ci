from numpy import random
from src.RandomGenerator.RandomGen import random_without_seed_decimal


def random_with_seed_decimal(start, end, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        rd_with_seed_decimal = random_without_seed_decimal(start, end)
        return rd_with_seed_decimal
    finally:
        random.set_state(state)
