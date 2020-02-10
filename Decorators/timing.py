# benchmarking or speed testing with decorators
from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        print(f"Time elapsed: {end - start}")
        return result
    return wrapper

@speed_test
def sum_nums():
    return sum(x for x in range(100000))

print(sum_nums())