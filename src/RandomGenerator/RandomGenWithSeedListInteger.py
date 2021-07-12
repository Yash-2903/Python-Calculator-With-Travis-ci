from numpy import random


def random_with_seed_list_integer(start, end, length, seed):
    state = random.get_state()
    random.seed(seed)
    try:
        int_list = random.randint(start, end, length)
        return int_list
    finally:
        random.set_state(state)
