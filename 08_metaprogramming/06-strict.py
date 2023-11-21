__doc__ = """Python is a dynamically typed language, which means that the type of a variable is determined at runtime.
However, it also features descriptor protocol, which allows to implement strict typing of class attributes.
Here's an example of a class that enforces strict typing of class attributes.

Starting from Python 3.6 descriptors can be implemented using `__set_name__` method
which is used for setting the name of the attribute in the class.

Rules of using meta-programming:
* Metaclass is always one
* Metaclass can be derived from other metaclass
* Real metaclass is the most derived metaclass
* Metaclass often inherits from `type` metaclass, however you can completely redefine its behavior yourself
* You can use base `abc.ABCMeta` metaclass to create abstract classes

Metaclass can be conflicting, if different classes in the inheritance hierarchy
have different metaclasses.
"""


# Example 1: Strict Integer using descriptor protocol
class Integer:
    def __init__(self, value=0):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{value} is not an integer")
        self.value = value

    def __delete__(self, instance):
        del self.value

    def __set_name__(self, owner, name):
        """
        Note: `type.__new__` calls `__set_name__` on the descriptor
        """
        self.name = name

    def __str__(self):
        return str(self.value)


x = Integer(10)
print(f"x == {x}")

x = 42
print(f"x == {x}")

y = Integer()
x = y
print(f"x == {x}")

# TODO: useful metaclasses, last 10 minutes of the video
