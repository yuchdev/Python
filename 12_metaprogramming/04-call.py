__doc__ = """In order to make instance callable, we need to implement __call__ method.
Class `type` use `__call__` method for creating new instances of the class.

Let's emulate it using metaprogramming (in reality its implementation is written in C).

This feature can be used in many powerful design patterns, e.g. Singleton, Factory, etc.
Let's implement Singleton using the same technique

Method `__new__` is static by definition, so we need to pass cls explicitly
It reminds of a constructor of the class, but actually it's not.
`__new__` is a static method that takes the class as a first parameter,
it's not necessarily to return a new instance of the class.
"""


# Example 1. Create a class using `type` metaclass
# noinspection PyPep8Naming, PyShadowingBuiltins, PyArgumentList
class type(object):

    def __call__(self, *args, **kwargs):
        """
        :param args: arguments to be passed to the constructor of the class
        :param kwargs: keyword arguments to be passed to the constructor of the class
        :return: instance of the class
        """
        # Create a new instance of the class
        obj = self.__new__(self, *args, **kwargs)
        # Initialize the instance of the class
        obj.__init__(*args, **kwargs)
        # Return the instance of the class
        return obj


class UseType:
    """
    We don't mention metaclass explicitly, because our `type` shadows the built-in `type`
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"UseType(a={self.a}, b={self.b})"


c = UseType(1, 2)
print(c)


# Example 2. Create a Singleton class
class Singleton:
    """
    Singleton is a design pattern that restricts the instantiation of a class to one object.
    It is useful when exactly one object is needed to coordinate actions across the system.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        :param args: arguments to be passed to the constructor of the class
        :param kwargs: keyword arguments to be passed to the constructor of the class
        :return: instance of the class
        """
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_params(self):
        print(f"a == {self.a}, b == {self.b}")


singleton = Singleton(1, 2)
print(singleton)
singleton.print_params()

singleton2 = Singleton(3, 4)
print(singleton2)
singleton2.print_params()


assert singleton is singleton2
