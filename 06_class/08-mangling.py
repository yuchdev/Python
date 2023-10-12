__doc__ = """There's no such thing as private members in Python
However, there's a convention to use _ in front of private members
Also, there's a name mangling mechanism, which is used to make
private members hidden, to use __ in front of private members
"""


class Counter:
    """
    I'm counter, I count stuff
    """
    def __init__(self, start=0):
        """
        _hidden is a private member, visible
        __mangled is a private member, hidden
        """
        self.counter = start
        self._hidden = 0
        self.__mangled = 0

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


c = Counter()
print(f"c.counter = {c.counter}")

# Warning: Access to a protected member _hidden of a class
# noinspection PyProtectedMember
print(f"c._hidden = {c._hidden}")

# AttributeError: 'Counter' object has no attribute '__mangled'
# print(f"c.__mangled = {c.__mangled}")
