import sys


# Arguments as a tuple
def foo(*args):
    print("Arguments as a tuple: args = {}, type = {}".format(args, type(args)))
    print("'Pointer' to first argument: *args = {}".format(*args))
    for arg in args:
        print("arg:", arg)


def could_be_empty(*args):
    """
    args could be empty
    """
    print("Empty: args = {}, type = {}".format(args, type(args)))


def at_least_one(first, *args):
    """
    Guarantee at least one argument
    """
    print("first = {}".format(first))
    for arg in args:
        print("arg:", arg)


def arguments():
    print("foo(1, 2, 3)")
    foo(1, 2, 3)
    print("could_be_empty()")
    could_be_empty()

    print("Guarantee at least one argument: at_least_one(1, 2, 3)")
    at_least_one(1, 2, 3)

    print("Convert collection to args: foo(*[1, 2, 3])")
    foo(*[1, 2, 3])

    print("set() converted to args in non-defined order: foo(*(1, 2, 3))")
    foo(*(1, 2, 3))


def default_args_function(low=0, high=255):
    print("low={}, high={}".format(low, high))


def default_args_infinity(low=float("-inf"), high=float("inf")):
    """
    Use float +/- infinity value
    """
    print("low={}, high={}".format(low, high))


# noinspection PyDefaultArgument
def init_defaults(iterable, seen=set()):
    """
    This default argument 'seen' initialized only once.
    It is static! And shared between all instances of init_defaults()
    Never change default values inside the function
    """
    print("iterable={}".format(iterable))
    for item in iterable:
        seen.add(item)
    print("seen={}".format(seen))


def trick_defaults(iterable, seen=None):
    """
    Trick how to avoid static init
    Create seen() inside function
    """
    seen = set(seen or [])
    for item in iterable:
        seen.add(item)
    print("seen={}".format(seen))


def defaults():
    print("default_args_function(low=0, high=255)")
    default_args_function()
    print("default_args_infinity(low=float('-inf'), high=float('inf'))")
    default_args_infinity()

    print("First defaults call")
    init_defaults([1, 2, 3])
    print("Second defaults call (seen shared between calls)")
    init_defaults([4, 5, 6])


def flatten(xs, depth=None):
    """
    Simple usage of key args
    """
    print("xs = {}, depth = {}".format(xs, depth))


def required_keyargs(*, xs,  depth=None):
    """
    After '*' symbol we require call of all arguments by name
    """
    print("xs = {}, depth = {}".format(xs, depth))


def keyargs():
    print("flatten(xs=1, depth=1)")
    flatten(xs=1, depth=1)
    print("flatten(1, 1)")
    flatten(1, 1)

    print("required_keyargs(xs=1, depth=1)")
    required_keyargs(xs=1, depth=1)
    print("required_keyargs(1, 1)")
    try:
        # noinspection PyArgumentList
        required_keyargs(1, 1)
    except TypeError as e:
        print("Key arguments required: {}".format(e))


def kwargs_foo(**kwargs):
    """
    kwargs unpacked as dictionary
    Could be useful for functions with many args
    """
    print("Arguments is dict: kwargs = {}, kwargs = {}".format(kwargs, type(kwargs)))
    print("'Pointer' to first argument: *kwargs = {}".format(*kwargs))
    if kwargs.get("verbose", True):
        print("verbose=True, verbose logging enabled")


def kwargs_show():
    kwargs_foo(verbose=True, xs=1)


def kwargs_unpack(*args, **kwargs):
    """
    This is complicated example of combined key args and unpacking
    """
    print("args = {}, kwargs = {}".format(args, kwargs))


def unpack():
    """
    Unpack of iterable into variables
    """
    print("Simple unpack syntax")
    x, y, z = [1, 2, 3]
    print("x={}, y={}, z={}".format(x, y, z))
    x, y, z = (1, 2, 3)
    print("x={}, y={}, z={}".format(x, y, z))
    x, y, z = "123"
    print("x={}, y={}, z={}".format(x, y, z))

    print("Extended unpack syntax")
    print("first, rest = [1, 2, 3, 4, 5]")
    first, *rest = [1, 2, 3, 4, 5]
    print("first = {}, rest = {}".format(first, rest))

    print("first, *rest, last = [1, 2, 3, 4, 5]")
    first, *rest, last = [1, 2, 3, 4, 5]
    print("first = {}, rest = {}, last = {}".format(first, rest, last))

    print("for a, *b in [[1, 2, 3], [4, 5, 6]]:")
    for a, *b in [[1, 2, 3], [4, 5, 6]]:
        print("a = {}, b = {}".format(a, b))

    print("Variety of arguments unpacking")
    print("kwargs_unpack(1, 2, *[3, 4], *[5], foo='bar', **{'baz': '42'}, boo=42)")
    kwargs_unpack(1, 2, *[3, 4], *[5], foo="bar", **{"baz": "42"}, boo=42)

    print("Unpack and replace")
    default_settings = {"host": "127.0.0.1", "port": 8080}
    print('default_settings = {"host": "127.0.0.1", "port": 8080}')
    print(default_settings)

    default_settings = {**default_settings, "port": 80}
    print('default_settings = {**default_settings, "port": 80}')
    print(default_settings)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
