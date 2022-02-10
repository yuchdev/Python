import sys
from functools import wraps


__doc__ = """Show examples of init_once decorator and decorator
that prevents calling function more than once with the same arguments.
"""


###############################################################################
# Step 1. When we perform initialization, we usually want to do it once
###############################################################################
def init_something01():
    """
    This function is called only once
    :return:
    """
    print("Init something")


def call_something01():
    """
    This function is called only once
    :return:
    """
    init_something01()


def show_initialize01():
    """
    We init twice
    :return:
    """
    call_something01()
    call_something01()


###############################################################################
# Step 2. Let's try to implement decorator for single call
###############################################################################
def call_once(func):
    """
    This decorator is used to make sure that the function is called only once
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.called:
            wrapper.called = True
            return func(*args, **kwargs)
    wrapper.called = False
    return wrapper


@call_once
def init_something02():
    """
    This function is called only once
    """
    print("Init something")


def call_something02():
    """
    This function is called only once
    """
    init_something02()


def show_initialize02():
    """
    We init once as expected
    """
    call_something02()
    call_something02()


###############################################################################
# Step 3. Now let's implement decorator that prevent calling function twice
# **with the same arguments**
###############################################################################
def call_once_with_args(func):
    """
    This decorator is used to make sure that the function is called only once
    with the same arguments
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # frozenset() is an inbuilt function which takes an iterable object
        # as input and makes them immutable
        key = (args, frozenset(kwargs.items()))
        if key not in wrapper.cache:
            wrapper.cache[key] = func(*args, **kwargs)
        return wrapper.cache[key]
    wrapper.cache = {}
    wrapper.__cache__ = wrapper.cache
    return wrapper


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
