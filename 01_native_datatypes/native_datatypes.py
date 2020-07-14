import fractions
import math
import sys


def show_import_path():
    """
    Show path where from import perform lookup
    """
    print('####################################')
    print('Import lookup path:', sys.path)
    # __name__ is a special built-in variable which evaluates to the module name
    # If a module is being run from command line__name__ is set to the string '__main__'
    print('Attribute __name__:', __name__)


def show_boolean():
    """
    Evaluate boolean
    """
    print('####################################')
    print('Evaluate boolean')
    size = 0
    # The result of the expression size < 0 is always a boolean
    print("size > 0 is", size > 0)
    print("size == 0 is", size == 0)
    print('Boolean implicitly converted to int, 42 + True =', 42 + True)


def show_numbers():
    """
    Evaluate numbers
    """
    print('####################################')
    print('Evaluate numbers')

    # 	You can use the type() function to check the type of any value or variable
    # 	Similarly, you can use the isinstance() function to check whether a value or variable is of a given type
    print(type(1))
    print(isinstance(1, int))
    print(isinstance(1.0, float))

    # Adding an int to a float yields a float
    print(type(1+1))
    print(type(1+1.0))


def show_conversions():
    """
    Converts int<->float
    """
    print('####################################')
    print('Convert numbers')
    # The int() function will truncate, not round
    # The int() function truncates negative numbers towards 0. It’s a true truncate function, not a floor function
    # Floating point numbers are accurate to 15 decimal places
    # Integers can be arbitrarily large
    print(int(2.9))
    print(int(-2.9))
    print(type(9999999999999999999))


def show_operations():
    """
    Simple math operations
    """
    print('####################################')
    print('Simple operations')
    # The / operator performs floating point division
    # The // operator performs a quirky kind of integer division
    # When the result is positive, you can think of it as truncating (not rounding)
    print(11/2)
    print(11//2)

    # When integer-dividing negative numbers, the // operator rounds up to the nearest integer
    print(-11//2)

    # The ** operator means raised to the power of
    print(4**2)

    # The % operator gives the remainder after performing integer division
    print(11 % 2)


def show_fractions():
    """
    Simple fractions
    """
    print('####################################')
    print('Simple fractions')

    # To start using fractions, import the fractions module
    x = fractions.Fraction(1, 3)
    print(x)

    # You can perform all the usual mathematical operations with fractions
    print(x**2)

    # The Fraction object will automatically reduce fractions (6/4) = (3/2)
    # Python has the good sense not to create a fraction with a zero denominator
    y = fractions.Fraction(6, 4)
    print(y)


def show_trigonometry():
    """
    Simple trigonometry operations
    """
    print('####################################')
    print('Simple trigonometry')
    print(math.pi)
    print(math.tan(math.pi/4))


def show_lists():
    """
    Lists operations
    List internal representation:
    https://www.laurentluce.com/posts/python-list-implementation/
    """
    print('####################################')
    print('Lists creation')

    # A list is an ordered set of items
    # Python keeps track of the list datatype internally
    a_list = ['a', 'b', 'mpilgrim', 'z', 'example']
    print(a_list)
    print(a_list[0])

    # A negative index accesses items from the end of the list counting backwards
    # The last item of any non-empty list is always a_list[-1]
    print(a_list[-1])

    # You can get a part of a list, called a slice, by specifying two indices
    # Slicing works if one or both of the slice indices is negative
    print(a_list[0:3])
    print(a_list[1:-1])
    print(a_list[-3:-1])

    print('####################################')
    print('Lists append')
    # There are four ways to add items to a list (other type)
    # you should be aware that list concatenation creates a second list in memory!
    a_list = a_list + [2.0, 3]
    print(a_list)

    # The append() method adds a single item to the end of the list
    # appending a list is adding single element of type 'list'
    a_list.append('4')
    print(a_list)

    # noinspection PyTypeChecker
    a_list.append([5, 6])
    print(a_list)

    # The extend() method takes one argument, a list,
    # and appends each of the items of the argument to the original list
    # noinspection PyTypeChecker
    a_list.extend([7, 8, 9])
    print(a_list)

    # The insert() method inserts a single item into a list
    # The first argument is the index of the first item in the list that will get bumped out of position
    a_list.insert(0, '0')
    print(a_list)

    print('####################################')
    print('Lists search')

    # counting
    print(a_list.count('0'))

    # in operator is slightly faster than using the count()
    print('0' in a_list)

    # The index() method finds the first occurrence of a value in the list. In this case
    # As you might not expect, if the value is not found in the list, the index() method will raise an exception
    print(a_list.index('0'))

    print('####################################')
    print('Lists removal')

    # del operator - by index
    # All items after the deleted item shift their positional index to “fill the gap” created by deleting the item
    del a_list[1]
    print(a_list)

    # The remove() method takes a value and removes the first occurrence of that value from the list
    # if item not found exception is thrown
    a_list.remove('b')
    print(a_list)

    # When called without arguments, the pop() list method removes the last item and returns the value
    print(a_list.pop())
    print(a_list)

    # You can pop arbitrary items from a list. Calling pop() on an empty list raises an exception
    print(a_list.pop(1))
    print(a_list)

    # an empty list is false
    if a_list:
        print(a_list)

    a_list.clear()
    if not a_list:
        print(a_list)

    # TODO:
    # Technically, all variables are passed by reference in Python, but have a semantics more like pass by value in C
    # A counterexample to your analogy is if you do
    # def f(my_list): my_list = [1, 2, 3]
    # With pass-by-reference in C, the value of the argument could change by calling that function
    # In Python, that function doesn't do anything
    # def f(my_list): my_list[:] = [1, 2, 3] would do something

    # One trick to quickly test if a type is mutable or not, is to use id() built-in function


def show_tuples():
    """
    Tuples operations
    """
    print('####################################')
    print('Tuples creation')

    # A tuple is an immutable list. A tuple can not be changed in any way once it is created
    # You can slice a tuple (because that creates a new tuple),
    # and you can check whether a tuple contains a particular value (because that doesn't change the tuple)
    a_tuple = ("a", "b", "mpilgrim", "z", "example")
    print(a_tuple)
    print(a_tuple[1:-1])

    # You can find elements in a tuple, since this doesn't change the tuple
    # You can also use the in operator to check if an element exists in the tuple
    print(a_tuple.index('example'))
    print('a' in a_tuple)

    # Tuples are faster than lists
    # It makes your code safer
    # Some tuples can be used as dictionary keys

    # To create a tuple of one item, you need a comma after the value
    one_tuple = ('item',)
    print(one_tuple)

    # Tuples can be converted into lists, and vice-versa
    print(list(a_tuple))

    # Here’s a cool programming shortcut: in Python, you can use a tuple to assign multiple values at once
    print('####################################')
    print('Assign multiple values')
    t = (2, 3, 4)
    x, y, z = t
    print(x, y, z)

    # tuple of variables
    (q, w, e) = range(3)
    print(q, w, e)


def show_sets():
    """
    Sets operations
    """
    print('####################################')
    print('Sets creation')
    # A set is an unordered 'bag' of unique values
    a_set = {1}
    print(type(a_set))
    print(a_set)

    # To create a set with one value, put the value in curly brackets ({})

    # You can also create a set out of a list
    a_list = ['a', 'b', 'mpilgrim', True, False, 42]
    a_set = set(a_list)
    print(a_set)
    print(a_list)

    # To create an empty set, call set() with no arguments
    # you can not create an empty set with two curly brackets
    # This actually creates an empty dictionary, not an empty set
    a_set2 = set()
    print(a_set2)

    print('####################################')
    print('Sets modification')

    # The add() method takes a single argument, which can be any datatype, and adds the given value to the set
    # If you try to add a value that already exists in the set, it will do nothing
    a_set.add(777)
    print(a_set)

    # The update() method takes one argument, a set, and adds all its members to the original set
    a_set2.update({2, 3, 4})
    print(a_set2)

    print('####################################')
    print('Sets removal')
    # There are three ways to remove individual values from a set

    # The first two, discard() and remove(), have one subtle difference
    # if the value doesn't exist in the set, the remove() method raises a KeyError exception
    a_set.discard('does_not_exists')
    print(a_set)

    a_set.remove(42)
    print(a_set)

    # Like lists, sets have a pop() method
    print(a_set.pop())
    print(a_set.pop())
    print(a_set.pop())
    print(a_set)
    # here is no way to control which value gets removed

    # math set operations support
    print('####################################')
    print('Sets operations')

    set_1 = {1, 2, 3}
    set_2 = {1, 2, 3, 4}

    print(set_1.intersection(set_2))
    print(set_1.difference(set_2))
    print(set_1.symmetric_difference(set_2))
    print(set_1.issubset(set_2))
    print(set_1.issuperset(set_2))


def show_dict():
    """
    Dictionary operations
    """
    print('####################################')
    print('Dictionary operations')

    # A dictionary is an unordered set of key-value pairs (based on hash)
    # The syntax is similar to sets, but instead of values, you have key-value pairs
    a_dict = {'server': 'db.diveintopython3.org', 'database': 'mysql'}

    # You can get values by key, but you can’t get keys by value
    print(a_dict)
    print(a_dict['server'])
    print(a_dict['database'])

    # Assigning a value to an existing key will wipe out the old value
    # Dictionary values can be any datatype, including integers, booleans, or even other dictionaries
    # And within a single dictionary, the values don’t all need to be the same type
    # Dictionary keys are more restricted, but they can be strings, integers, and a few other types
    a_dict['user'] = 'mark'
    print(a_dict)

    print(len(a_dict))
    print('user' in a_dict)

    # None is a special constant in Python. It is a null value
    a_dict['None'] = None
    print(a_dict)


def show_string():
    """
    String representations
    https://rushter.com/blog/python-strings-and-memory/
    """
    pass


if __name__ == '__main__':
    show_boolean()

