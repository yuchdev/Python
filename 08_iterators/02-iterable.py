__doc__ = """Iterable and Iterator examples
* iterators support 'in' operator, in works in O(n) time
* net every sequences can be iterated twice (e.g. network connection)
* second form of iter() function accepts callable and sentinel (see implementation below)

Python abstracts away many of the complexities of working with iterators 
by automatically performing the necessary operations behind the scenes.
The use of explicit iterators in `for` loops would add complexity and reduce code readability,
so we use them implicitly
"""


class RangeIterator:
    """
    Range Iterator class
    """
    def __init__(self, start, end):
        """
        In standard library, start and stop have default values
        """
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        """
        Iterator
        """
        return self

    def __next__(self):
        """
        Next method
        """
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


class Range:
    """
    Range class
    """
    def __init__(self, start, end):
        """
        In standard library, start and stop have default values
        """
        self.start = start
        self.end = end

    def __iter__(self):
        """
        Iterator
        """
        return RangeIterator(self.start, self.end)


# Ranges accepted in for loops
for i in Range(0, 10):
    print(i)

# in works in O(n) time
# Always think about performance
is_42 = 42 in Range(0, 100)

# Ranges accepted in functions-consumers that accept collections, e.g. sum()
r = Range(0, 10)
accumulated = sum(r)


# TODO: sort it out later
def range2(start, stop):
    """
    Range function
    """
    def step():
        """
        Step function access start through closure
        """
        nonlocal start
        start += 1
        return start - 1
    return iter(step, stop)