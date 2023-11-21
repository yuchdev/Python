__doc__ = """Import in Python is a way to include other modules.
"""

# This is what we import from this module by `from small_module import *`
__all__ = ['GLOBAL_VALUE', 'small_function', 'SmallClass']


GLOBAL_VALUE = 0


def small_function():
    """
    Small function
    """
    print("Small function")
    return 0


class SmallClass:
    def __init__(self):
        print("Small class")
        self.value = 0
