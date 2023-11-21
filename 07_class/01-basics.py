import sys

__doc__ = """Classes were introduced in Python 2.2, that is quite late
for a programming language. Python is not object-oriented language,
but rather object-based. It means that you can use objects, but you
don't have to. You can write procedural code in Python, but you can
also write object-oriented code. It's up to you.
"""


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


# In Python no keyword new is used
counter = Counter()
print(counter.get())

counter.increment()
print(counter.get())
