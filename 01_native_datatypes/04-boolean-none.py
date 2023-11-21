__doc__ = """Python None type and the Boolean (bool) type

None Type

Purpose:
    None is a special constant in Python that represents the absence of a value or a null value.
    It is often used to signify that a variable or a function does not return any meaningful result.

Creation:
    There is only one instance of None in Python, and it is often used as a singleton.
    Variables can be assigned the value None to indicate a lack of a specific value.

Common Use Cases:
    Initializing variables or placeholders.
    Representing the default value of function arguments.


Comparison:
    None is often used in comparisons to check if a variable has been assigned a value or not

Type:
    None has its own type, NoneType

bool Type:

Purpose:
    The bool type represents Boolean values: True or False.
    Booleans are fundamental for making logical decisions in programming.

Creation:
    Booleans can be created through comparison operations, logical operations, or by explicitly assigning the values True or False.

Boolean Operations:
    Boolean values can be combined using logical operations (and, or, not).

Type:
    The bool type is a subclass of the int type. True is equivalent to 1, and False is equivalent to 0

Truthy and Falsy Values:
    In Python, some values are considered truthy or falsy in boolean contexts
    For example, 0, None, and empty containers (like an empty list or an empty string) are falsy, 
    while non-zero numbers, non-empty containers, and non-None values are truthy.
"""

my_variable = None


def my_function(arg=None):
    pass


print(type(None))


result = 5 > 3  # result is True
flag = False

x = True
y = False
result_and = x and y  # False
result_or = x or y    # True
result_not = not x    # False

print(type(True))   # Output: <class 'bool'>
