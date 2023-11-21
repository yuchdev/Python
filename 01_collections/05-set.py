import sys


def create():
    """
    Create sets
    """
    print('Sets creation')

    # A set is an unordered 'bag' of unique values
    # Based of hash table
    a_set = {1, 2, 3}
    print("a_set =", a_set)
    print("type(a_set) =", type(a_set))

    # You can also create a set out of a list
    a_list = ['a', 'b', 'Python', True, False, 42]
    a_set = set(a_list)
    print("a_list =", a_list)
    print("set(a_list) =", a_set)

    # To create an empty set, call set() with no arguments
    # you can not create an empty set with two curly brackets
    # This actually creates an empty dictionary, not an empty set
    a_set2 = set()
    print("set() =", a_set2)


def append():
    print('Sets modification')
    a_set = {1, 2, 3}
    print("a_set =", a_set)

    # The add() method takes a single argument, which can be any datatype,
    # and adds the given value to the set
    # If you try to add a value that already exists in the set, it will do nothing
    a_set.add(777)
    print("a_set.add(777) =", a_set)

    # The update() method takes one argument, a set, and adds all its members to the original set
    a_set.update({2, 3, 4})
    print("a_set2.update({2, 3, 4}) =", a_set)


def remove():
    print('Sets removal')
    a_set = {1, 2, 3}
    print("a_set =", a_set)
    # There are three ways to remove individual values from a set

    # The first two, discard() and remove(), have one subtle difference
    # if the value doesn't exist in the set, the remove() method raises a KeyError exception
    # discard() does nothing
    does_not_exists = 42
    a_set.discard(does_not_exists)

    try:
        a_set.remove(42)
    except KeyError as _:
        print("a_set.remove(42):", a_set)

    # Like lists, sets have a pop() method
    print(a_set.pop())
    print(a_set.pop())
    print(a_set.pop())
    print("a_set.pop() 3 times: ", a_set)
    # here is no way to control which value gets removed


def operations():
    print('Sets operations')

    set_1 = {1, 2, 3}
    set_2 = {1, 2, 3, 4}
    print("set_1 =", set_1)
    print("set_2 =", set_2)

    # & \ ^ issubset issuperset
    print("set_1.intersection(set_2) =", set_1.intersection(set_2))
    print("set_1.difference(set_2) =", set_1.difference(set_2))
    print("set_1.symmetric_difference(set_2) =", set_1.symmetric_difference(set_2))
    print("set_1.issubset(set_2) =", set_1.issubset(set_2))
    print("set_1.issuperset(set_2) =", set_1.issuperset(set_2))

    print("set1 | set_2 =", set_1 | set_2)
    print("set1 & set_2 =", set_1 & set_2)
    print("set1 - set_2 =", set_1 - set_2)
    print("set1 ^ set_2 =", set_1 ^ set_2)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
