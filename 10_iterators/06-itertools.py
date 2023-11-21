import sys
from itertools import islice, count, cycle, repeat, tee
from itertools import dropwhile, takewhile, chain
from itertools import product, permutations, combinations, combinations_with_replacement
from itertools import groupby

__doc__ = """Module itertools provides a number of iterator building blocks
They are usually memory-efficient fast, and elegant.
They can efficiently replace cycles with multiple nested loops.

* Slicing with islice() accept any iterable object, and returns an iterator
* Infinite iterators
    * function count() returns an iterator that produces consecutive integers indefinitely
    * function cycle() returns an iterator that makes the iterable repeat
    * function repeat() returns an iterator that produces the same value each time
    * function dropwhile() and takewhile() perform filtering operations based on a test function
    * function chain() makes it easy to process several iterables as a single sequence
* tee() function is used to create multiple independent iterators from a single iterable.
* tee() can be helpful when you need to iterate through the same data more than once 
* Combinatoric iterators
    * function product() computes the cartesian product of input iterables
    * function permutations() returns successive r length permutations of elements in the iterable
    * function combinations() returns successive r length combinations of elements in the iterable
    * function combinations_with_replacement() returns successive r length combinations of elements in the iterable
* object groupby() returns an iterator that produces sets of values organized by a common key
"""


def show_slice():
    # islice() works with any iterable, and returns an iterator that returns
    # selected items from the iterable by index
    sliced_list = list(islice(range(10), 5))
    print(f"list(islice(range(10), 5)) = {sliced_list}")

    # sum of islice
    sum_islice = sum(islice(range(10), 5))
    print(f"sum(islice(range(10), 5)) = {sum_islice}")


# Infinite iterators
def take(n, iterable):
    """
    Return first n items of the iterable as a list
    :param n:
    :param iterable:
    :return:
    """
    return list(islice(iterable, n))


def show_infinite():
    taken1 = take(3, range(10))
    print(f"take(3, range(10)) = {taken1}")

    # function count() returns an iterator that produces consecutive integers indefinitely.
    # The first number can be passed as an argument (default is 0)
    taken_count = take(5, count(10, 0.1))
    print(f"take(5, count(10, 0.1)) = {taken_count}")

    # function cycle() returns an iterator that makes the iterable repeat
    taken_cycle = take(10, cycle('ABCD'))
    print(f"take(10, cycle('ABCD')) = {taken_cycle}")

    # function repeat() returns an iterator that produces the same value each time
    taken_repeat = take(10, repeat(10, 3))
    print(f"take(10, repeat(10, 3)) = {taken_repeat}")


# dropwhile() and takewhile() make it easy to take slices from an iterator based on a predicate
def show_while():
    dropwhile_list = list(dropwhile(lambda x: x < 5, range(10)))
    print(f"list(dropwhile(lambda x: x < 5, range(10))) = {dropwhile_list}")

    takewhile_list = list(takewhile(lambda x: x < 5, range(10)))
    print(f"list(takewhile(lambda x: x < 5, range(10))) = {takewhile_list}")


def show_chain():
    chain_list = list(chain('ABC', range(2)))
    print(f"list(chain('ABC', range(2))) = {chain_list}")

    chain_list2 = list(chain(enumerate('ABC')))
    print(f"list(chain(enumerate('ABC'))) = {chain_list2}")


def show_tee():
    """
    tee() function is used to create multiple independent iterators from a single iterable.
    This can be helpful when you need to iterate through the same data more than once
    without affecting the other iterators.
    """
    # Create an iterable
    original_data = [1, 2, 3, 4, 5]

    # Use tee to create two independent iterators
    iterator1, iterator2 = tee(original_data, 2)

    # Iterate through the first iterator
    print("Iterator 1:")
    for item in iterator1:
        print(item)

    # Iterate through the second iterator
    print("Iterator 2:")
    for item in iterator2:
        print(item)


def show_combinatorics():
    product_list = list(product('ABC', range(2)))
    print(f"list(product('ABC', range(2))) = {product_list}")

    permutations_list = list(permutations('ABC', 2))
    print(f"list(permutations('ABC', 2)) = {permutations_list}")

    combinations_list = list(combinations('ABC', 2))
    print(f"list(combinations('ABC', 2)) = {combinations_list}")

    combinations_with_replacement_list = list(combinations_with_replacement('ABC', 2))
    print(f"list(combinations_with_replacement('ABC', 2)) = {combinations_with_replacement_list}")


def show_groupby():
    """
    function groupby() returns an iterator that produces sets of values organized by a common key
    It groups adjacent elements with the same key into sub-iterables, making it easier
    to process data based on some criteria.
    The elements should be sorted or grouped by the key you want to group them by.
    """
    # Sample data (must be sorted/grouped by the key)
    data = [
        ('A', 1),
        ('B', 2),
        ('A', 3),
        ('C', 4),
        ('B', 5),
        ('A', 6),
    ]
    print(f"data = {data}")

    # Sort the data by the key
    data.sort(key=lambda x: x[0])
    print(f"sorted data = {data}")

    # Use groupby to group data by the key
    grouped_data = groupby(data, key=lambda x: x[0])
    print(f"grouped_data={list(grouped_data)} type={type(grouped_data)}")

    print("Iterate over the grouped data")
    for key, group in grouped_data:
        print(f"Key: {key}")
        for item in group:
            print(f"  {item}")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
