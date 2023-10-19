import sys

__doc__ = """Generators in Python work as follows:
* generator is a function that returns an object (iterator) which we can iterate over (one value at a time)
* generator defined like a normal function
* generator uses yield instead of return
* when we reach yield, generator will return the value and pause the execution
* next() function resumes the execution
* generator function can have multiple yield statements
* when generator reach the end of the function, StopIteration exception is raised
* generator can be infinite

Advantages of generators:
* easy to implement
* memory efficient
* represent infinite stream
* implement pipelines (e.g. data processing)
"""


# Implement range generator
def range_gen(start, end):
    """
    Range generator
    """
    current = start
    while current < end:
        yield current
        current += 1


# Use range generator
def use_range_gen():
    for i in range_gen(0, 10):
        print(i)


# Generator may contain multiple yield statements
# In this case we resume after each yield
def range_bidirectional(start, end):
    """
    Range generator
    """
    current = start
    while current < end:
        print("Before first yield")
        yield current
        print("After first yield")
        current += 1
    while current > start:
        print("Before second yield")
        yield current
        print("After second yield")
        current -= 1


def use_range_bidirectional():
    for i in range_bidirectional(0, 2):
        print(i)


# One more example: function unique()
def unique(iterable, seen=None):
    """
    Unique generator
    """
    seen = set(seen or [])
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


# Use unique generator
def use_unique():
    for i in unique([1, 2, 3, 1, 2, 3, 1, 2, 3]):
        print(i)


# Example: function map()
def map_gen(func, iterable, *args):
    """
    Map generator
    Note: map() in Python accept arbitrary number of iterables,
    which we represent as *args
    """
    for item in zip(iterable, *args):
        yield func(item, *args)


# Use map generator
def use_map_gen():
    for i in map_gen(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]):
        print(i)


# Example: function chain()
def chain_gen(*iterables):
    """
    Chain generator
    Function chain() used to chain multiple iterables
    It works in "lazy" way - we don't touch next iterable until we finish previous one
    """
    for iterable in iterables:
        for item in iterable:
            yield item


def use_chain_gen():
    iterable1 = [1, 2, 3]
    iterable2 = [4, 5, 6]
    for i in chain_gen(iterable1, iterable2):
        print(i)


# Example: infinite generator
def infinite_gen(start=0):
    """
    Infinite generator
    """
    while True:
        yield start
        start += 1


def use_infinite_gen():
    """
    When you use infinite generator, you should break the loop manually
    """
    for i in infinite_gen():
        print(i)
        if i > 10:
            break


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
