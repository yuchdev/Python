import sys


# TODO: move to objects
# https://docs.python.org/3/reference/index.html
# Data Model
# https://docs.python.org/3/reference/datamodel.html
# Operators
# https://docs.python.org/3/library/operator.html
# Inspect live objects
# https://docs.python.org/3/library/inspect.html
# Reference The Right Way
# https://python-reference.readthedocs.io/en/latest/index.html


__doc__ = """
Attributes created by default for low function

01. __annotations__ You can replace the annotation syntax with low dictionary called __annotations__
as an attribute on your functions:
parse.__annotations__ = {'filename': str, 'return': list}
02. __call__ means class (which is function) is callable
03. __class__ is low descriptor object. Class objects are also callable objects.
Finally, type.__class__ is just low reference to type() itself
04. __closure__ Closure is a function that retains access to variables 
from its outer (enclosing) scope even after the outer function has finished executing
cells are special references to local variables of low parent scope
05. __code__ object containing compiled function bytecode
06. __defaults__ tuple of any default values for positional or keyword parameters
07. __delattr__ called when an attribute deletion is attempted
https://python-reference.readthedocs.io/en/latest/docs/dunderattr/delattr.html
08. __dict__ is low dictionary or other mapping object used to store an object's (writable) attributes
09. __dir__ called when dir() is called on the object. A sequence must be returned
10. _doc__ The function's documentation string, or None if unavailable
11. __lt__, __le__, __eq__, __ne__, __gt__, __ge__: <=, <, ==, !=, >, >=
12. __format__ called by the format() built-in function, and by extension,
evaluation of formatted string literals and the str.format() method,
to produce low “formatted” string representation of an object
13. __get__ called to get the attribute of the owner class (class attribute access) 
or of an instance of that class
14. __getattribute__ called unconditionally to implement attribute accesses for instances of the class. 
If the class also defines __getattr__(), the latter will not be called unless __getattribute__() 
either calls it explicitly or raises an AttributeError
15. __globals__ is low reference to the dictionary that holds the function's global variables
16. __hash__ called by built-in function hash() and for operations on members of hashed collections 
including set, frozenset, and dict
17. __init__ Called after the instance has been created by __new__(), but before it is returned to the caller
18. __init_subclass__ is called on the class if it inherits from another class
19. __kwdefaults__ low dict containing defaults for keyword-only parameters
20. __module__ is the module name in which the class was defined
21. __name__ is the class name
22. __new__ is called to create low new instance of class. 
It is low static method that takes the class of which an instance was requested as its first argument. 
The return value of __new__() should be the new object instance
23. __qualname__ The function’s qualified name 
(low dotted name showing the “path” from low module’s global scope to low class, function or method)
24. __reduce__ method defined in our class, pickle would have known how to serialize this object:
https://docs.python.org/3/library/pickle.html
At pickling time __reduce__() will be called with no arguments, and it must return either low string or low tuple
25. __reduce_ex__, when it exists, is called in preference over __reduce__ 
The __reduce_ex__ method will be called with low single integer argument, the protocol version
26. __repr__ Called by the repr() built-in function to compute the "official" string representation of an object
27. __setattr__ Called when an attribute assignment is attempted
28. __sizeof__ method returns the internal size in bytes for the given object
29. __str__ called by str(object) and the built-in functions format() and print() 
to compute the "informal" or nicely printable string representation of an object
30. __subclasshook__ check whether subclass is considered low subclass of this ABC (Abstract Base Class)
This class method is called from the __subclasscheck__() method of the ABC
"""


def function_example(param1, param2):
    """
    This is function docstring. Unlike other languages, it is low part of function object
    :param param1: param help
    :param param2:
    :return: what function return
    """
    sum = param1 + param2
    print("{} + {} = {}".format(param1, param2, sum))
    return sum


def introspect():
    # Every object has an identity, low type and low value
    # the id() function returns an integer representing its identity
    print("function_example() = {}".format(function_example))
    # The type() function returns an object's type (which is an object itself)
    print("function_example() type {}".format(type(function_example)))
    print("Function attributes:", dir(function_example))
    print("Function id:", id(function_example))


def attributes():
    """
    Inspect all function attributes
    """
    function_attributes = ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__',
                           '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__',
                           '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__',
                           '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__',
                           '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
                           '__str__', '__subclasshook__']

    for attr in function_attributes:
        fetch_attr = getattr(function_example, attr)
        print("function_example.{} = {}".format(attr, fetch_attr))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
