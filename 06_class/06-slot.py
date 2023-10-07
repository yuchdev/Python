__doc__ = """Slots are a way to declare class members in advance
It is useful for performance reasons, as it saves memory.
You can't declare __dict__ if you use __slots__,
so you can't add new attributes to the class
"""


class Point2D:
    """
    __slots__ is a tuple of strings, which are names of class members
    You can have only x and y in this class
    Slots can be inherited like any other class
    """
    __slots__ = ("x", "y")

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        # AttributeError: 'Point2D' object has no attribute 'z'
        # self.z = 3

    def __str__(self):
        return f"({self.x}, {self.y})"


p = Point2D(1, 2)
print(p)

# AttributeError: 'Point2D' object has no attribute 'z'
# p.z = 3
