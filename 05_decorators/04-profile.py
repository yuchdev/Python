import sys
import time
from functools import wraps, lru_cache, singledispatch

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


def fib01(n):
    """
    Recursive Fibonacci sequence generator.
    """
    return 1 if n == 1 else 1 if n == 2 else fib01(n - 1) + fib01(n - 2)


@profile
def show_profile01():
    """
    Get some large Fibonacci numbers.
    """
    print(f"fib01({30}) = {fib01(30)}")


###############################################################################
# Step 2. Now let's implement decorator that prevent calling function twice
# **with the same arguments**
###############################################################################
def call_once_with_args(func):
    """
    This decorator is used to make sure that the function is called only once
    with the same arguments, otherwise using returned value from cache.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # frozenset() is an inbuilt function which takes an iterable object
        # as input and makes them immutable
        key = (args, frozenset(kwargs.items()))
        if key not in wrapper.cache:
            wrapper.cache[key] = func(*args, **kwargs)
        return wrapper.cache[key]
    wrapper.cache = {}
    wrapper.__cache__ = wrapper.cache
    return wrapper


# Decorators could be combined
@profile
@call_once_with_args
def fib02(n):
    """
    Recursive Fibonacci sequence generator with caching call once decorator
    """
    return 1 if n == 1 else 1 if n == 2 else fib01(n - 1) + fib01(n - 2)


def show_profile02():
    """
    Second run is much faster
    """
    print(f"1 fib02({30}) = {fib02(30)}")
    print(f"2 fib02({30}) = {fib02(30)}")


# TODO:
# Step 3. Decorator call_once_with_args() exists in the Python standard library
# and called functools.lru_cache()
# https://docs.python.org/3/library/functools.html#functools.lru_cache
def call_once_with_args_lru(func):
    """
    This decorator is used to make sure that the function is called only once
    with the same arguments, otherwise using returned value from cache
    Utilize functools.lru_cache() decorator
    """
    def decorator(cached_func):
        @lru_cache(maxsize=sys.maxsize)
        def wrapper(*args, **kwargs):
            return cached_func(*args, **kwargs)
        return wrapper
    return decorator


@profile
@call_once_with_args_lru
def fib03(n):
    """
    Recursive Fibonacci sequence generator with caching call once decorator
    """
    return 1 if n == 1 else 1 if n == 2 else fib01(n - 1) + fib01(n - 2)


def show_profile03():
    """
    Second run is much faster
    """
    print(f"1 fib03({30}) = {fib03(30)}")
    print(f"2 fib03({30}) = {fib03(30)}")


# Step 4. Decorator functools.singledispatch() adds a method to an existing type
# which we do not define
@singledispatch
def process_data(data):
    raise NotImplementedError("This function should be implemented for specific data types")


@process_data.register(int)
def _(data):
    print(f"Processing integer: {data}")


@process_data.register(str)
def _(data):
    print(f"Processing string: {data}")


@process_data.register(list)
def _(data):
    print(f"Processing list: {data}")


def show_profile04():
    process_data(42)  # Calls the int implementation
    process_data("Hello,")  # Calls the str implementation
    process_data([1, 2, 3])  # Calls the list implementation


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
