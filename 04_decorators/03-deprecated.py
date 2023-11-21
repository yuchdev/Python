import sys
from functools import wraps
import warnings


__doc__ = "Example of deprecation decorator"


###############################################################################
# Step 1. Let's try to implement the decorator warning us
# about the deprecated functionality
###############################################################################
def deprecated(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        warnings.warn(f"Function {func.__name__}() is deprecated", category=DeprecationWarning)
        return func(*args, **kwargs)
    return wrapper


@deprecated
def deprecate01():
    print("Init something")


def show_deprecated01():
    deprecate01()


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
