# Function to test
import itertools


def rle(iterable):
    """
    Run-length encoding

    >>> list(rle('AABBB'))
    [('A', 2), ('B', 3)]

    >>> list(rle(''))
    []
    """
    for item, group in itertools.groupby(iterable):
        yield item, sum(1 for _ in group)


def sort(iterable):
    """
    In-place sorts iterable

    >>> sort([1, 2, 3])
    [1, 2, 3]

    >>> sort([3, 2, 1])
    [1, 2, 3]
    """
    iterable.sort()
    return iterable
