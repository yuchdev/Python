__doc__ = """Python descriptors are a way to implement attributes with special behavior. 
They are created by extending the "descriptor protocol".

E.g. we want to create a class that only accepts integer values between 0 and 100.
We overload the `__set__` method of the descriptor protocol.
Descriptor protocol support overloading of `__get__`, `__set__` and `__delete__` methods.
Do not confuse with the `__getattr__` and `__setattr__` methods of the object protocol.
 In practice, you would use __get__ when you want to define custom behavior for attribute access, 
typically within a descriptor, while you would use __getattr__ when you want to handle attribute access 
for undefined attributes, typically within a class definition.

Attribute Lookup Order

Example 1. `obj.x` is translated to:
1. If obj.__dict__ contains x, return obj.__dict__['x']
2. If Obj.__dict__ contains __get__, return Obj.__dict__.__get__(obj, Obj)
3. If Obj.__dict__ contains x, return x.__get__(obj)

Example 2. `instance.foobar: Class` is translated to:
1. Class.__getattribute__(instance, 'foobar')
2. If 'foobar' in Class.__dict__:
    a. If Class.__dict__['foobar'] defines __get__ and __set__, return Class.__dict__['foobar'].__get__(instance, Class)
    b. If Class.__dict__['foobar'] defines __get__ skip check (3)
3. If 'foobar' in instance.__dict__:
    a. Return instance.__dict__['foobar']
    b. Otherwise repeat (2)
4. If 'foobar' in Class.__dict__:
    a. If Class.__dict__['foobar'] defines __get__, return Class.__dict__['foobar'].__get__(instance, Class)
    b. Otherwise return Class.__dict__['foobar']
5. If 'foobar' not in Class.__dict__ return Class.__getattr__('foobar')
6. Raise AttributeError

Data and Non-Data Descriptors
Data descriptors are descriptors that define both `__get__` and `__set__` methods, 
and they always win over `obj.__dict__['x']`
Non-data descriptors are descriptors that define only `__get__` method, and they always "lose" to `obj.__dict__['x']`
"""


def square(x):
    """
    This works for function, but not for methods!
    """
    return x**2


print(f"square.__get__ is {square.__get__}")
print(f"f = square.__get__(10, int) == {square.__get__(10, int)}")

f = square.__get__(10, int)
print(f"f() == {f()}")


# Example 1: Cached Property
class CachedProperty:
    """
    Decorator that converts a method with a single self argument into a property cached on the instance
    """
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        print(f"obj is {obj}, cls is {cls}")
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value
