__doc__ = """
"""


class Counter:
    """
    I'm counter, I count stuff
    """
    # Class attributes are shared by all instances of a class
    # It's an analogy to static variables in C++
    all_counters = []

    def __init__(self, start=0):
        """
        No explicit declaration of attributes in __init__
        """
        self.counter = start
        self.all_counters.append(self)

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


c1 = Counter()
c2 = Counter(10)
c3 = Counter(100)
assert len(Counter.all_counters) == 3

# You can assess class attributes from instances and from the class itself
assert c1.all_counters is c2.all_counters is Counter.all_counters


# Attributes resolution order
class A:

    x = 1

    def __init__(self):
        self.x = 2


print(f"A.x: {A.x}")
a = A()
print(f"a.x: {a.x}")

# Bound methods is a special case of attributes
# They are functions, but they are bound to an instance
# So they have access to instance attributes
print(f"c1.increment: {c1.increment}")
print(f"c1.increment.__func__: {c1.increment.__func__}")
print(f"c1.increment.__self__: {c1.increment.__self__}")
print(f"Counter.increment: {Counter.increment}")
