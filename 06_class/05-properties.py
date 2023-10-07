__doc__ = """Property is a special kind of attribute that has a getter and a setter
It is achieved by using decorator @property,
and the resulting object is called descriptor, which behaves like a data field
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

    @property
    def is_zero(self) -> bool:
        return self.counter == 0


c = Counter()
print(c.get())
c.increment()
print(c.is_zero)
