__doc__ = """
"""


class Counter:
    """
    I'm counter, I count stuff
    """
    def __init__(self, start=0):
        """
        In Python __init__ is not a constructor, but rather initializer
        By the moment __init__ is called, object is already created
        """
        # Python class members don't have declaration
        # Instead, they are created on the fly
        # However, there's a convention to declare them in __init__
        self.counter = start

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1
