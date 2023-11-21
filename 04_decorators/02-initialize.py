import sys
from functools import wraps, singledispatch

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
    Init twice
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
    Init once as expected
    """
    call_something02()
    call_something02()


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
