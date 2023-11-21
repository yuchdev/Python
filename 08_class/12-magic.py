__doc__ = """Python classes feature a lot of "magic" methods
Including 
- comparison: __lt__, __le__, __eq__, __ne__, __gt__, __ge__
- arithmetic: __add__, __sub__, __mul__, __truediv__, __floordiv__, __mod__, __pow__, __matmul__
- augmented assignment: __iadd__, __isub__, __imul__, __itruediv__, __ifloordiv__, __imod__, __ipow__, __imatmul__
- unary: __neg__, __pos__, __abs__, __invert__
- type conversion: __int__, __float__, __complex__, __bool__, __str__, __repr__
- container: __len__, __getitem__, __setitem__, __delitem__, __contains__
- context manager: __enter__, __exit__
- attribute access: __getattr__, __setattr__, __delattr__, __getattribute__
- callable: __call__
- iterator: __iter__, __next__
- async iterator: __aiter__, __anext__
- async context manager: __aenter__, __aexit__
- async callable: __acall__
"""

import functools


class Counter:
    """
    This version of Counter class implements comparison operators
    """
    def __init__(self, start=0):
        """
        By the moment __init__ is called, object is already created
        """
        self.counter = start

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1

    def __repr__(self):
        return f"Counter({self.counter})"

    def __str__(self):
        return f"Counter: {self.counter}"

    def __lt__(self, other):
        """
        < operator
        """
        return self.counter < other.counter

    def __le__(self, other):
        """
        <= operator
        """
        return self.counter <= other.counter

    def __eq__(self, other):
        """
        == operator
        """
        return self.counter == other.counter

    def __ne__(self, other):
        """
        != operator
        """
        return self.counter != other.counter

    def __gt__(self, other):
        """
        > operator
        """
        return self.counter > other.counter

    def __ge__(self, other):
        """
        >= operator
        """
        return self.counter >= other.counter

    def __hash__(self):
        """
        Objects are equal if they have the same hash
        """
        return hash(self.counter)

    def __add__(self, other):
        """
        + operator
        You have to implement 2 methods to support + operator:
        - __add__ for Counter + Counter
        - __radd__ for int + Counter
        """
        if isinstance(other, Counter):
            return Counter(self.counter + other.counter)
        elif not isinstance(other, int):
            raise TypeError(f"Cannot add Counter and {type(other)}")
        else:
            return Counter(self.counter + other)

    def __radd__(self, other):
        """
        + operator with reversed operands, to add Counter to integer
        Right-hand operand is always passed as an argument
        """
        return self + other


c1 = Counter(4)
c2 = Counter(5)

print(f"c1 < c2 = {c1 < c2}")
print(f"c1 <= c2 = {c1 <= c2}")
print(f"c1 == c2 = {c1 == c2}")
print(f"c1 != c2 = {c1 != c2}")

dict_counter = {c1: 1, c2: 2}
print(f"dict_counter = {dict_counter}")

print(f"c1 + c2 = {c1 + c2}")
print(f"1 + c2 = {1 + c2}")
print(f"c1 + 3 = {c1 + 3}")


@functools.total_ordering
class CounterFunc:
    """
    Actually, there's decorator @functools.total_ordering that can be used
    to implement all comparison operators by implementing only __eq__ and __lt__
    """
    def __init__(self, start=0):
        self.counter = start

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1

    def __repr__(self):
        return f"Counter({self.counter})"

    def __str__(self):
        return f"Counter: {self.counter}"

    def __eq__(self, other):
        return self.counter == other.counter

    def __lt__(self, other):
        return self.counter < other.counter


c3 = CounterFunc(4)
c4 = CounterFunc(5)

print(f"c3 < c4 = {c3 < c4}")
print(f"c3 <= c4 = {c3 <= c4}")
print(f"c3 == c4 = {c3 == c4}")
print(f"c3 != c4 = {c3 != c4}")
print(f"c3 > c4 = {c3 > c4}")
print(f"c3 >= c4 = {c3 >= c4}")
print(f"c3 <= c4 = {c3 <= c4}")
