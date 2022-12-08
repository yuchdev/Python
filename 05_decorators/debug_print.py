import sys
from functools import partial
from functools import wraps

__doc__ = """Show examples of debug print decorators.
From naive to production implementation.
"""


###############################################################################
# Step 01. Manual debug print of function max01()
def max01(*args):
    """
    manually finds the largest argument
    :param args:
    :return:
    """
    ret = 0
    print(f"args: {args}")
    for arg in args:
        ret = ret if arg < ret else arg
    print(f"max({args}) = {ret}")
    return ret


def show_max01():
    """
    Example of function max01()
    """
    max01(1, 2, 3, 4, 5)


###############################################################################
# Step 02. Using high-order function-decorator for debug print
# Decorators are high-order functions that add some functionality
# to other functions by returning a new (wrapped) function
def debug_print02(func):
    """
    Decorator for debug print
    :param func:
    :return:
    """
    # This part is executed once for each function
    # You can use this to do some initialisation and check global flags
    def wrapper(*args, **kwargs):
        # This part is executed every time the wrapped function is called
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        ret = func(*args, **kwargs)
        print(f"{func.__name__}() returned {ret}")
    return wrapper


@debug_print02
def max02(*args):
    """
    Finds the largest argument using decorator debug_print02()
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max02():
    """
    Example of function max02()
    """
    max02(1, 2, 3, 4, 5)

    # However, as we can see here, the decorator debug_print02() replaces
    # the __name__, __doc__, and __module__ of the decorated function
    print(f"max02 name is: {max02.__name__}")
    print(f"max02 doc is: {max02.__doc__}")
    print(f"max02 module is: {max02.__module__}")


###############################################################################
# Step 03. Using high-order function-decorator for debug print
# with replacing __name__, __doc__, and __module__ of the decorator
# with respected values of the decorated function
def debug_print03(func):
    """
    Decorator for debug print with replacing __name__, __doc__, and __module__
    :param func:
    :return:
    """
    # This part is executed once for each function
    # You can use this to do some initialisation and check global flags
    def wrapper(*args, **kwargs):
        # This part is executed every time the wrapped function is called
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        ret = func(*args, **kwargs)
        print(f"{func.__name__}() returned {ret}")

    # Replace __name__, __doc__, and __module__ with respected values of the decorated function
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    wrapper.__module__ = func.__module__
    return wrapper


@debug_print03
def max03(*args):
    """
    Finds the largest argument using decorator debug_print03()
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max03():
    """
    Example of function max03()
    """
    max03(1, 2, 3, 4, 5)
    # Now we can see that the __name__, __doc__, and __module__ of the decorated function
    # are assigned to the wrapper function
    print(f"max03 name is: {max03.__name__}")
    print(f"max03 doc is: {max03.__doc__}")
    print(f"max03 module is: {max03.__module__}")


###############################################################################
# Step 04. Let's create a generic function that updates the __name__, __doc__, and __module__
# for both wrapper and decorated functions
def update_decorator(decorate_func, wrapper_func):
    """
    Updates the __name__, __doc__, and __module__ of the decorated function
    :param decorate_func:
    :param wrapper_func:
    :return:
    """
    # Replace __name__, __doc__, and __module__ with respected values of the decorated function
    for attr in ["__name__", "__doc__", "__module__"]:
        setattr(wrapper_func, attr, getattr(decorate_func, attr))
    wrapper_func.__decorate_func__ = decorate_func
    return wrapper_func


def debug_print04(func):
    """
    Decorator for debug print with replacing __name__, __doc__, and __module__
    using generic function update_decorator()
    :param func:
    :return:
    """
    # This part is executed once for each function
    # You can use this to do some initialisation and check global flags
    def wrapper(*args, **kwargs):
        # This part is executed every time the wrapped function is called
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        ret = func(*args, **kwargs)
        print(f"{func.__name__}() returned {ret}")
    update_decorator(func, wrapper)
    return wrapper


@debug_print04
def max04(*args):
    """
    Finds the largest argument using decorator debug_print04()
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


###############################################################################
# Step 05. There's a high-order function in functools called partial(func, /, *args, **keywords)
# that returns a new partial object which when called will behave like func
# called with the positional arguments args and keyword arguments keywords.
# The partial() is used for partial function application which “freezes” some portion of a function’s arguments
# and/or keywords resulting in a new object with a simplified signature
# Let's use it in debug_print05()
def debug_print05(func):
    """
    Decorator for debug print with replacing __name__, __doc__, and __module__
    using generic function update_decorator()
    :param func:
    :return:
    """
    # Return decorator to update __name__, __doc__, and __module__
    # of the decorator (wrapper)
    update_decorator_description = partial(update_decorator, func)

    @update_decorator_description
    def wrapper(*args, **kwargs):
        # This part is executed every time the wrapped function is called
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        ret = func(*args, **kwargs)
        print(f"{func.__name__}() returned {ret}")

    return wrapper


@debug_print05
def max05(*args):
    """
    Finds the largest argument using decorator debug_print05()
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max05():
    """
    Example of function max05()
    """
    max05(1, 2, 3, 4, 5)
    # Now we can see that the __name__, __doc__, and __module__ of the decorated function
    # are assigned to the wrapper function
    print(f"max05 name is: {max05.__name__}")
    print(f"max05 doc is: {max05.__doc__}")
    print(f"max05 module is: {max05.__module__}")


###############################################################################
# Step 06. In fact, both update_wrapper() and update_decorator_description()
# are implemented in functools as functools.wraps(wrapper)
def debug_print06(func):
    """
    Use functools.wraps(wrapper) to wrap inner function wrapper()
    :return:
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}")
        ret = func(*args, **kwargs)
        print(f"{func.__name__}() returned {ret}")
    return wrapper


@debug_print06
def max06(*args):
    """
    Finds the largest argument using decorator debug_print06()
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max06():
    """
    Example of function max06()
    """
    max06(1, 2, 3, 4, 5)
    # Now we can see that the __name__, __doc__, and __module__ of the decorated function
    # are assigned to the wrapper function
    print(f"max06 name is: {max06.__name__}")
    print(f"max06 doc is: {max06.__doc__}")
    print(f"max06 module is: {max06.__module__}")


###############################################################################
# Step 7. Let's implement a decorator tha redirects debug print to stderr
# instead of stdout.
###############################################################################
def trace_stderr01(stream=sys.stderr):
    """
    Decorator that prints a function's name, its arguments, and its return
    values to a stream (by default stderr).
    """

    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            stream.write(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}\n")
            result = func(*args, **kwargs)
            stream.write(f"{func.__name__}({args}, {kwargs}) returned {result}\n")
            return result

        return wrapper

    return decorate


# We can choose sys.stderr or sys.stdout to redirect the output
@trace_stderr01(sys.stderr)
def max07(*args):
    """
    Finds the largest argument using decorator trace_stderr01.
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max07():
    """
    Shows the result of max07
    """
    print(max07(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(f"max07 name is {max01.__name__}")
    print(f"max07 doc is {max01.__doc__}")
    print(f"max07 module is {max01.__module__}")


###############################################################################
# Step 8. Let's now try to pass a function and a stream to a decorator
###############################################################################
def trace_stderr02(func=None, stream=sys.stderr):
    """
    Decorator that prints a function's name, its arguments, and its return
    values to a stream (by default stderr).
    """
    # If we don't pass a function, then we're returning a decorator
    # Thus our decorator can both with and without arguments
    if func is None:
        return partial(trace_stderr02, stream=stream)

    @wraps(func)
    def wrapper(*args, **kwargs):
        stream.write(f"Calling {func.__name__}() with args: {args} and kwargs: {kwargs}\n")
        result = func(*args, **kwargs)
        stream.write(f"{func.__name__}({args}, {kwargs}) returned {result}\n")
        return result

    return wrapper


@trace_stderr02
def max08(*args):
    """
    Finds the largest argument using decorator trace_stderr02.
    :param args:
    :return:
    """
    ret = 0
    for arg in args:
        ret = ret if arg < ret else arg
    return ret


def show_max08():
    """
    Shows the result of max08
    """
    print(max08(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    print(f"max08 name is {max02.__name__}")
    print(f"max08 doc is {max02.__doc__}")
    print(f"max08 module is {max02.__module__}")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
