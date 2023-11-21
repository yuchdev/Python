__doc__ = """Iteration protocol
* Iteration in Python is based on the iterator protocol: a container object (such as a list)
  must provide a way to repeatedly access its contents until all the elements have been exhausted.
  This is achieved by implementing __iter__() and __next__() methods
* End of container is indicated by raising StopIteration exception in __next__()
  which is an example of bad design, because we use exceptions for control flow
* Python 3.7 introduced __anext__() method which returns an awaitable object
* function next(iterator, default) can be used to iterate over an iterator

Iterable and Iterator
There are 2 distinct concepts: iterable and iterator
    - Iterable is an object that can be iterated over
    - Iterator is an object that implements __iter__() and __next__() methods
Example:
    >>> iterable = [1, 2, 3]
    >>> iterator = iter(iterable)
* Iterator is an iterable, but iterable is not an iterator (not a language limitation, but a design decision)
"""


class Iterator:
    def __init__(self, data):
        """
        :param data: anything iterable
        """
        print(f'Iterator.__init__{data}')
        self.data = data
        self.index = 0

    def __iter__(self):
        """
        Iterator is an iterable, so __iter__() should return an iterator
        This is required to allow both iterable and iterator to be used in for loop
        :return: iterator itself
        """
        print('Iterator.__iter__')
        return self

    def __next__(self):
        """
        Return next element of the iterator
        """
        print('Iterator.__next__')
        if self.index >= len(self.data):
            print('Iterator. StopIteration')
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


class Iterable:
    def __init__(self, data):
        """
        :type data: list
        :param data: iterable of elements
        """
        print(f'Iterable.__init__{data}')
        self.data = data

    def __iter__(self):
        """
        Return an iterator
        """
        print('Iterable.__iter__')
        return Iterator(self.data)


# Usage:
for item in Iterable([1, 2, 3]):
    print(item)


# This construction is equivalent to the following:
iterator = iter(Iterable([4, 5, 6]))
# (You don't have to explicitly define iterator to use for loop)
while True:
    try:
        item = next(iterator)
    except StopIteration:
        # Exception is used for control flow, which is a bad design
        print('StopIteration')
        break
    print(item)
