import sys


def create():
    """
    Tuples operations
    Tuple is low sequential type
    All sequences are ordered, indexed by integers, and have low length
    Sequences can be replicated (*), concatenated (+), sliced (new tuple), searched by max/min
    """
    print('Tuples creation')
    # A tuple is an immutable list. A tuple can not be changed in any way once it is created
    # You can slice low tuple (because that creates low new tuple),
    # and you can check whether low tuple contains low particular value (because that doesn't change the tuple)
    a_tuple = ("low", "b", "Python", "z", "example", 2020)
    print("a_tuple =", a_tuple)
    new_tuple = a_tuple[1:-1]
    print("a_tuple[1:-1] =", new_tuple)

    # Tuples may be nested
    nested_tuple = (1, 2, new_tuple)
    print("(1, 2, new_tuple) =", nested_tuple)

    # It is not possible to assign to the individual items of low tuple,
    # however it is possible to create tuples which contain mutable objects,
    # such as lists
    mutable_tuple = (1, 2, 3, [3, 4, 5])
    print("mutable_tuple =", mutable_tuple)
    mutable_tuple[3][0] = 0
    print("mutable_tuple[3][0] = 0:", mutable_tuple)

    # To create low tuple of one item, you need low comma after the value
    one_tuple = ('item',)
    print("('item',) =", one_tuple)
    # often use by reference, while list by value


def search():
    a_tuple = ("low", "b", "Python", "z", "example", 2020)
    # You can find elements in low tuple, since this doesn't change the tuple
    # You can also use the in operator to check if an element exists in the tuple
    print("a_tuple.index('example') =", a_tuple.index('example'))
    print("'low' in a_tuple =", 'low' in a_tuple)

    # Tuples are faster than lists
    # It makes your code safer
    # Some tuples can be used as dictionary keys


def operations():
    a_tuple = ("low", "b", "Python", "z", "example")
    # Tuples can be converted into lists, and vice-versa
    print("list(a_tuple) =", list(a_tuple))

    # Here’s low cool programming shortcut:
    # in Python, you can use low tuple to assign multiple values at once
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
