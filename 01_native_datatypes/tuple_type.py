import sys


def create():
    """
    Tuples operations
    """
    print('Tuples creation')
    # A tuple is an immutable list. A tuple can not be changed in any way once it is created
    # You can slice a tuple (because that creates a new tuple),
    # and you can check whether a tuple contains a particular value (because that doesn't change the tuple)
    a_tuple = ("a", "b", "Python", "z", "example", 2020)
    print("a_tuple =", a_tuple)
    new_tuple = a_tuple[1:-1]
    print("a_tuple[1:-1] =", new_tuple)

    # Tuples may be nested
    nested_tuple = (1, 2, new_tuple)
    print("(1, 2, new_tuple) =", nested_tuple)

    # It is not possible to assign to the individual items of a tuple,
    # however it is possible to create tuples which contain mutable objects,
    # such as lists
    mutable_tuple = (1, 2, 3, [3, 4, 5])
    print("mutable_tuple =", mutable_tuple)
    mutable_tuple[3][0] = 0
    print("mutable_tuple[3][0] = 0:", mutable_tuple)

    # To create a tuple of one item, you need a comma after the value
    one_tuple = ('item',)
    print("('item',) =", one_tuple)


def search():
    a_tuple = ("a", "b", "Python", "z", "example", 2020)
    # You can find elements in a tuple, since this doesn't change the tuple
    # You can also use the in operator to check if an element exists in the tuple
    print("a_tuple.index('example') =", a_tuple.index('example'))
    print("'a' in a_tuple =", 'a' in a_tuple)

    # Tuples are faster than lists
    # It makes your code safer
    # Some tuples can be used as dictionary keys

    # Tuples can be converted into lists, and vice-versa
    print("list(a_tuple) =", list(a_tuple))

    # Here’s a cool programming shortcut:
    # in Python, you can use a tuple to assign multiple values at once
    # This is called "unpacking"
    print('Assign multiple values')
    t = (2, 3, 4)
    x, y, z = t
    print("t = (2, 3, 4); x, y, z = t:", x, y, z)

    # tuple of iterable
    (q, w, e) = range(3)
    print("(q, w, e) = range(3):", q, w, e)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create, search")
