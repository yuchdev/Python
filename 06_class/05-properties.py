__doc__ = """Property is a special kind of attribute that has a getter and a setter
It is achieved by using decorator @property,
and the resulting object is called descriptor, which behaves like a data field

The process of choosing the best data representation in Python is following:
- Never use getter/setter like in C++/Java
- Use public attributes if you don't have invariant
- Use properties if you have invariant and read-only attributes
- Use __slots__ if you have a lot of objects
- Use dict/NamedTuple if you have a lot of attributes
- Use method is you have side-effects, a lot of code, or you need to pass arguments 
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


class Temperature:

    def __init__(self, *, celsius: float = 0):
        self._celsius = 0

    @property
    def celsius(self) -> float:
        return self._celsius

    @celsius.setter
    def celsius(self, value: float):
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value: float):
        self._celsius = (value - 32) * 5 / 9

t = Temperature()
t.celsius = 20
print(t.celsius)
print(t.fahrenheit)
t.fahrenheit = 68
print(t.celsius)
print(t.fahrenheit)
