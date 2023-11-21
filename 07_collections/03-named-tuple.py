import sys
from collections import namedtuple
from typing import NamedTuple

__doc__ = """Named tuples are a memory efficient way to store data when you don't need
the capabilities of a full class.
Named tuples are implemented in the collections module
"""


def show_named_tuple():
    """
    Create named tuple
    Named tuple can be used for dynamic creation of types
    """
    # Point is a type
    Point2D = namedtuple('Point', ['x', 'y'])

    # after declaration Point behaves like a class
    p = Point2D(11, y=22)
    print(p[0] + p[1])
    x, y = p
    print(x, y)
    print(p.x + p.y)
    print(Point2D(x=11, y=22))

    # _replace() method allows you to create a new named tuple with some of the fields updated
    # underscore is used to avoid possible conflict with field named "replace"
    p2 = p._replace(x=33)
    print(p2)


# You can inherit from named tuple
class Point(namedtuple('Point', ['x', 'y'])):
    """
    namedtuple is a class
    """
    __slots__ = ()

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y, self.hypot)


class Point2(NamedTuple):
    """
    NamedTuple is a class
    """
    x: float
    y: float

    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return 'Point: x=%6.3f y=%6.3f hypot=%6.3f' % (self.x, self.y, self.hypot)


def show_class():
    """
    Inheritance from named tuple
    """
    p = Point(3, 4)
    print(p)
    print(p.x, p.y, p.hypot)
    print(isinstance(p, Point))
    print(isinstance(p, tuple))

    p2 = Point2(3, 4)
    print(p2)
    print(p2.x, p2.y, p2.hypot)
    print(isinstance(p2, Point2))
    print(isinstance(p2, tuple))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
