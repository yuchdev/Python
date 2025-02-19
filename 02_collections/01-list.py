import sys
import random
from dataclasses import dataclass


def create():
    """
    Lists operations
    List can be used and have appropriate API to behave as stack or queue

    List internal representation in C:

    struct PyListObject {
        // list header
        PyObject_VAR_HEAD
        // array of pointers to the list elements
        PyObject **ob_item;
        // number of allocated elements (could be less than actual elements)
        Py_ssize_t allocated;
    };

    Standard list is slow, because it uses pointers to value of polymorphic type
    Fast option is NumPy list, which is true C array

    List is a sequential type
    All sequences are ordered, indexed by integers, and have a length
    Sequences can be replicated (*), concatenated (+), sliced,
    sorted, searched by max/min

    Do not copy list! This operation is extremely slow
    Python lacks linked list (use deque instead)
    """
    print('Lists creation')

    # A list is an ordered set of items
    # Python keeps track of the list datatype internally
    # Use a list when the order of the data matters
    a_list = ['a', 'b', 'atatat', 'z', 'example', 'Python']
    print("a_list=", a_list)
    print("a_list[0]=", a_list[0])

    # A negative index accesses items from the end of the list counting backwards
    # The last item of any non-empty list is always a_list[-1]
    print("a_list[-1] =", a_list[-1])

    # You can get a part of a list, called a slice, by specifying two indices
    # Include rule is [begin, end)
    # Slicing works if one or both of the slice indices is negative
    print("a_list[0:3] =", a_list[0:3])
    print("a_list[1:-1] =", a_list[1:-1])
    print("a_list[-3:-1] =", a_list[-3:-1])

    # Slicing with step [start:stop:step]
    print("a_list[0:5:2] =", a_list[0:5:2])

    # create random list
    rnd_list = random.sample(range(1, 100), 10)
    print("random.sample(range(1, 100), 10) = {}".format(rnd_list))


# noinspection GrazieInspection
def append():
    print('Lists append')
    a_list = ['a', 'b', 'atatat', 'z', 'example', 'Python']

    print("Merge list:")
    # There are four ways to add items to a list (other type)
    # you should be aware that list concatenation creates a second list in memory!
    a_list = a_list + [2.0, 3]
    print("a_list + [2.0, 3] =", a_list)

    print("Replicate list:")
    a_list *= 2
    print("a_list *= 2 =", a_list)

    print("append() method adds a single item:")
    # The 'append()' method adds a single item to the end of the list
    # appending a list is adding single element of type 'list'
    # It has O(1) complexity because it just adds a pointer to the end of the pre-allocated list
    a_list.append('4')
    print("a_list.append('4') =", a_list)

    print("Append list as item:")
    # noinspection PyTypeChecker
    a_list.append([5, 6])
    print("a_list.append([5, 6]) =", a_list)

    print("extend() method is merge to original list:")
    # The 'extend()' method takes one argument, a list,
    # and appends each of the items of the argument to the original list
    # noinspection PyTypeChecker
    # It has O(k) complexity because it has to iterate over the list to add each element
    a_list.extend([7, 8, 9])
    print("a_list.extend([7, 8, 9]) =", a_list)

    print("The insert() method inserts a single item into a position in the list")
    # The first argument is the index of the first item in the list that will get bumped out of position
    # It has O(n) complexity because it has to shift all elements after the inserted element
    a_list.insert(0, '0')
    print("a_list.insert(0, '0') =", a_list)

    # The join() method returns a string concatenated
    # with the elements of list of strings (or any iterable)
    str_list = ["0", "1", "2", "3"]
    s: str = "."
    joined_list = s.join(str_list)
    print("joined_list = s.join(str_list)", joined_list)


def search():
    print('Lists search')
    a_list = ['a', 'b', 'atatat', 'z', 'example', 'Python', '0', 0]
    print("a_list =", a_list)

    # counting
    print("a_list.count('0') =", a_list.count('0'))

    # in operator is slightly faster than using the count()
    print("'0' in a_list is", '0' in a_list)

    # The index() method finds the first occurrence of a value in the list. In this case
    # As you might not expect, if the value is not found in the list,
    # the index() method will raise an exception
    print("a_list.index('0') =", a_list.index('0'))

    # index() could have a hint (begin, [end])
    print("a_list.index('0', 3) =", a_list.index('0', 3))


def remove():
    print('Lists removal')
    a_list = ['a', 'b', 'atatat', 'z', 'example', 'Python', '0', 0]
    print("a_list =", a_list)

    # del operator - by index
    # All items after the deleted item shift their positional index
    # to “fill the gap” created by deleting the item
    # It is easy with C pointers as list elements implementation
    del a_list[1]
    print("del a_list[1] =", a_list)

    # The remove() method takes a value and removes the first occurrence of that value from the list
    # if item not found exception is thrown
    a_list.remove('0')
    print("a_list.remove('0')", a_list)

    # When called without arguments, the pop() list method removes the last item and returns the value
    pop_item = a_list.pop()
    print("print(a_list.pop()) = {0}, item pop={1}".format(a_list, pop_item))

    # You can pop arbitrary items from a list. Calling pop() on an empty list raises an exception
    pop_item = a_list.pop(1)
    print("print(a_list.pop(1))= {0}, item pop={1}".format(a_list, pop_item))

    # an empty list is false
    if a_list:
        print("List is not empty:", a_list)

    a_list.clear()
    if not a_list:
        print("clear() method called, list now is empty:", a_list)


def append_ref(items):
    print("def append_ref(items); items = {}".format(items))
    print("items.append(4)")
    items.append(4)
    print("items = {}".format(items))


def by_reference():
    """
    Technically, all variables are passed by reference in Python
    With pass-by-reference, the value of the argument could change by calling that function
    """
    a_list = [1, 2, 3]
    print("1: a_list = {}".format(a_list))
    print("append_ref(a_list)")
    append_ref(a_list)
    print("2: a_list = {}".format(a_list))


def by_value():
    """
    my_list[:] would pass by value
    One trick to quickly test if a type is mutable or not, is to use id() built-in function (?)
    """
    a_list = [1, 2, 3]
    print("1: a_list = {}".format(a_list))
    print("append_ref(a_list[:])")
    append_ref(a_list[:])
    print("2: a_list = {}".format(a_list))


def operations():
    a_list = ['a', 'b', 'atatat', 'z', 'example', 'Python', '0']
    print("a_list =", a_list)
    # Sort the items of the list in place
    a_list.sort()
    print("a_list.sort() =", a_list)
    # Implementation:
    # sort() is guaranteed to be stable
    # Python sort has optimization looking for almost sorted sub-list,
    # and later apply merge sort to them

    # Reverse the elements of the list in place
    a_list.reverse()
    print("a_list.reverse() =", a_list)
    # reverse() is heavy operation, because it's in-place operation
    # reverse through comprehension instead
    reversed_list = [x for x in reversed(a_list)]

    print("reversed_list = [x for x in reversed(a_list)] =", reversed_list)

    # one more way to reverse list
    reversed_list = a_list[::-1]

    print("reversed_list = a_list[::-1] =", reversed_list)

    # The enumerate function adds an extra counter value to iteration
    # A good example of using enumerate()
    # is tracking line numbers while reading a file
    for index, val in enumerate(a_list):
        print("%d=%s" % (index, val))

    # Composite key (sort by first name, then by length of last name)
    names = ["John Smith", "Alice Johnson", "Bob Johnson", "Emma Brown", "Michael White"]
    sorted_names = sorted(names, key=lambda fullname: (fullname.split()[0], len(fullname.split()[1])))
    for name in sorted_names:
        print(name)


@dataclass(frozen=True)
class DataclassFrozen:
    """
    Dataclass is a class with a few restrictions
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y


def show_dataclass():
    """
    Dataclass is a class with a few restrictions
    """
    dc1 = DataclassFrozen(1, 2)
    dc2 = DataclassFrozen(1, 3)
    print(dc1)
    # frozen dataclass is immutable, allows hash and being used as key in dict
    print(hash(dc1))
    dataclass_dict = {dc1: 1}
    print(dataclass_dict)

    dataclass_dict[dc2] = 2
    print(dataclass_dict)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create, append, search, remove, operations")
