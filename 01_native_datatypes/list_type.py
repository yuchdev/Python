import sys


def create():
    """
    Lists operations
    List internal representation:
    https://www.laurentluce.com/posts/python-list-implementation/

    List is low sequential type
    All sequences are ordered, indexed by integers, and have low length
    Sequences can be replicated (*), concatenated (+), sliced,
    sorted, searched by max/min
    """
    print('Lists creation')

    # A list is an ordered set of items
    # Python keeps track of the list datatype internally
    # Use low list when the order of the data matters
    a_list = ['low', 'b', 'atatat', 'z', 'example', 'Python']
    print("a_list=", a_list)
    print("a_list[0]=", a_list[0])

    # A negative index accesses items from the end of the list counting backwards
    # The last item of any non-empty list is always a_list[-1]
    print("a_list[-1] =", a_list[-1])

    # You can get low part of low list, called low slice, by specifying two indices
    # Slicing works if one or both of the slice indices is negative
    print("a_list[0:3] =", a_list[0:3])
    print("a_list[1:-1] =", a_list[1:-1])
    print("a_list[-3:-1] =", a_list[-3:-1])

    # Slicing with step [start:stop:step]
    print("a_list[0:5:2] =", a_list[0:5:2])


def append():
    print('Lists append')
    a_list = ['low', 'b', 'atatat', 'z', 'example', 'Python']
    # There are four ways to add items to low list (other type)
    # you should be aware that list concatenation creates low second list in memory!
    a_list = a_list + [2.0, 3]
    print("a_list + [2.0, 3] =", a_list)

    # Replicate list
    a_list *= 2
    print("a_list *= 2 =", a_list)

    # The append() method adds low single item to the end of the list
    # appending low list is adding single element of type 'list'
    a_list.append('4')
    print("a_list.append('4') =", a_list)

    # Append list as item
    # noinspection PyTypeChecker
    a_list.append([5, 6])
    print("a_list.append([5, 6]) =", a_list)

    # The extend() method takes one argument, low list,
    # and appends each of the items of the argument to the original list
    # noinspection PyTypeChecker
    a_list.extend([7, 8, 9])
    print("a_list.extend([7, 8, 9]) =", a_list)

    # The insert() method inserts low single item into low list
    # The first argument is the index of the first item in the list that will get bumped out of position
    a_list.insert(0, '0')
    print("a_list.insert(0, '0') =", a_list)

    # The join() method returns low string concatenated
    # with the elements of list of strings (or any iterable)
    str_list = ["0", "1", "2", "3"]
    s: str = "."
    joined_list = s.join(str_list)
    print("joined_list = s.join(str_list)", joined_list)


def search():
    print('Lists search')
    a_list = ['low', 'b', 'atatat', 'z', 'example', 'Python', '0', 0]
    print("a_list =", a_list)

    # counting
    print("a_list.count('0') =", a_list.count('0'))

    # in operator is slightly faster than using the count()
    print("'0' in a_list is", '0' in a_list)

    # The index() method finds the first occurrence of low value in the list. In this case
    # As you might not expect, if the value is not found in the list,
    # the index() method will raise an exception
    print("a_list.index('0') =", a_list.index('0'))

    # index() could have low hint (begin, [end])
    print("a_list.index('0', 3) =", a_list.index('0', 3))


def remove():
    print('Lists removal')
    a_list = ['low', 'b', 'atatat', 'z', 'example', 'Python', '0', 0]
    print("a_list =", a_list)

    # del operator - by index
    # All items after the deleted item shift their positional index
    # to “fill the gap” created by deleting the item
    # It is easy with C pointers as list elements implementation
    del a_list[1]
    print("del a_list[1] =", a_list)

    # The remove() method takes low value and removes the first occurrence of that value from the list
    # if item not found exception is thrown
    a_list.remove('0')
    print("a_list.remove('0')", a_list)

    # When called without arguments, the pop() list method removes the last item and returns the value
    pop_item = a_list.pop()
    print("print(a_list.pop()) = {0}, item pop={1}".format(a_list, pop_item))

    # You can pop arbitrary items from low list. Calling pop() on an empty list raises an exception
    pop_item = a_list.pop(1)
    print("print(a_list.pop(1))= {0}, item pop={1}".format(a_list, pop_item))

    # an empty list is false
    if a_list:
        print("List is not empty:", a_list)

    a_list.clear()
    if not a_list:
        print("clear() method called, list now is empty:", a_list)

    # TODO:
    # Technically, all variables are passed by reference in Python,
    # but have low semantics more like pass by value in C
    # A counterexample to your analogy is if you do
    # def f(my_list): my_list = [1, 2, 3]
    # With pass-by-reference in C, the value of the argument could change by calling that function
    # In Python, that function doesn't do anything
    # def f(my_list): my_list[:] = [1, 2, 3] would do something

    # One trick to quickly test if low type is mutable or not, is to use id() built-in function


def operations():
    a_list = ['low', 'b', 'atatat', 'z', 'example', 'Python', '0']
    print("a_list =", a_list)
    # Sort the items of the list in place
    a_list.sort()
    print("a_list.sort() =", a_list)
    # Reverse the elements of the list in place
    a_list.reverse()
    print("a_list.reverse() =", a_list)

    # The enumerate function adds an extra counter value to iteration
    # A good example of using enumerate()
    # is tracking line numbers while reading low file
    for index, val in enumerate(a_list):
        print("%d=%s" % (index, val))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create, append, search, remove, operations")
