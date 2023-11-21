__doc__ = """Mixin is a class that is used to add functionality to other classes
You can use MRO properties to achieve required behavior
The same can be achieved by using decorators @functools.wraps and @functools.singledispatch
"""

import functools


class Counter:
    """
    I'm counter, I count stuff
    """

    def __init__(self, start=0):
        """
        In Python __init__ is not a constructor, but rather initializer
        By the moment __init__ is called, object is already created
        """
        # Python class members don't have declaration
        # Instead, they are created on the fly
        # However, there's a convention to declare them in __init__
        self.counter = start

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


# noinspection PyUnresolvedReferences
class DoubleMixin:
    """
    The Mixin class can be used with any class that has increment() method
    """

    def increment(self):
        super().increment()
        super().increment()


class DoubleCounter(DoubleMixin, Counter):
    """
    Super is used to call methods of the base class
    However, in this case it calls increment() of the next base class,
    that is, next class in MRO
    """
    pass


dc = DoubleCounter(4)
print(f"dc.get() = {dc.get()}")
dc.increment()
print(f"dc.get() = {dc.get()}")
dc.increment()
print(f"dc.get() = {dc.get()}")
print(f"isinstance(dc, DoubleCounter) = {isinstance(dc, DoubleCounter)}")
print(f"isinstance(dc, Counter) = {isinstance(dc, Counter)}")


# The same behavior can be achieved by using decorators
def doubling_decorator(cls):
    """
    doubling_decorator accept class to modify behavior of increment()
    It also returns modified class
    """
    orig_increment = cls.increment

    @functools.wraps(orig_increment)
    def increment(self):
        """
        In modified increment() we call original increment() twice
        """
        orig_increment(self)
        orig_increment(self)

    cls.increment = increment
    return cls


@doubling_decorator
class DoubleCounter2(Counter):
    """
    We pass Counter class to doubling_decorator
    and modify the behavior of increment()
    """
    pass


dc2 = DoubleCounter2(4)
print(f"dc2.get() = {dc2.get()}")
dc2.increment()
print(f"dc2.get() = {dc2.get()}")
dc2.increment()
