__doc__ = """Let's emulate decorator @staticmethod using metaprogramming
Python @staticmethod is a decorator that is used to define a static method for a function in a class.
It's quite useless in general, because you very rarely need to call a static method and not a regular function.

Decorator @classmethod is much more useful, because it allows you to call a method of a class,
instead of a method of an instance of a class.
Let's emulate it as well 

We may use @classmethod to create a factory method, which is a method that returns an instance of a class.
"""


# noinspection PyPep8Naming, PyShadowingBuiltins
class staticmethod(object):
    """
    Python @staticmethod is a decorator that is used to define a static method for a function in a class.
    It is just a regular function that is defined inside a class.
    """

    def __init__(self, function):
        self.function = function

    def __get__(self, obj, cls=None):
        return self.function


# noinspection PyPep8Naming,PyShadowingBuiltins
class classmethod(object):
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, cls=None):
        if cls is None:
            cls = type(obj)

        def new_function(*args, **kwargs):
            return self.function(cls, *args, **kwargs)

        return new_function


# Example 1: Static Method
class UseStatic:
    def __init__(self):
        pass

    @staticmethod
    def foo():
        print("foo")


UseStatic.foo()


# Example 2: Class Method
class UseClassMethod:
    def __init__(self):
        pass

    @classmethod
    def foo(cls):
        print(f"cls is {cls}")


UseClassMethod.foo()
