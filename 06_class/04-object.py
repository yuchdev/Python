__doc__ = """Class duality:
* Class in Python is an object
* Class in Python is a statement 
"""

class Counter:
    """
    I'm counter, I count stuff
    """
    all_counters = []

    def __init__(self, start=0):
        """
        No explicit declaration of attributes
        """
        self.counter = start
        self.all_counters.append(self)

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


# Class in Python is actually an object too
print(f"Counter is an object: {isinstance(Counter, object)}")
print(f"Counter.__name__: {Counter.__name__}")
print(f"Counter.__doc__: {Counter.__doc__}")
print(f"Counter.__module__: {Counter.__module__}")
print(f"Counter.__bases__: {Counter.__bases__}")


class Weird:
    """
    Class is also a statement, so it can be used in expressions
    """
    fib0, fib1 = 0, 1
    for _ in range(10):
        fib0, fib1 = fib1, fib0 + fib1


# We see that class statements are executed
print(f"Weird.fib0: {Weird.fib0}")
print(f"Weird.fib1: {Weird.fib1}")
