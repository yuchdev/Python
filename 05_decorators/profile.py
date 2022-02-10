import sys
import time
from functools import wraps


__doc__ = "Time profiling decorator"


def profile(func):
    """
    Decorator to time a function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print("{} took {} seconds".format(func.__name__, elapsed))
        wrapper.__n_calls += 1
        wrapper.__total_time += elapsed
        return result
    wrapper.__n_calls = 0
    wrapper.__total_time = 0
    return wrapper


def fib(n):
    """
    Recursive Fibonacci sequence generator.
    """
    return 1 if n == 1 else 1 if n == 2 else fib(n - 1) + fib(n - 2)


@profile
def show_slow():
    """
    Get some large Fibonacci numbers.
    """
    for i in range(1, 30):
        print(f"fib({i}) = {fib(i)}")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
