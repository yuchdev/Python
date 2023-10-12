__doc__ = """
"""


class Counter:
    """
    I'm counter, I count stuff
    """
    def __init__(self, start=0):
        """
        In Python __init__ is not a constructor, but rather initializer
        By the moment __init__ is called, object is already created
        """
        # Python class members don't have declaration
        # Instead, they are created on the fly
        # However, there's a convention to declare them in __init__
        self.counter = start

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


class SquaredCounter(Counter):
    def get(self) -> int:
        return self.counter * self.counter


c1 = Counter(4)
c2 = SquaredCounter(4)
print(f"c1.get() = {c1.get()}")
print(f"c2.get() = {c2.get()}")

# isinstance() is a way to check if object is an instance of a class
print(f"isinstance(c1, Counter) = {isinstance(c1, Counter)}")
print(f"isinstance(c2, Counter) = {isinstance(c2, Counter)}")
print(f"isinstance(c1, SquaredCounter) = {isinstance(c1, SquaredCounter)}")
print(f"isinstance(c2, SquaredCounter) = {isinstance(c2, SquaredCounter)}")

# issubclass() is a way to check if class is a subclass of another class
print(f"issubclass(SquaredCounter, Counter) = {issubclass(SquaredCounter, Counter)}")
print(f"issubclass(Counter, SquaredCounter) = {issubclass(Counter, SquaredCounter)}")

# issubclass() access tuple for comparing multiple classes
print(f"issubclass(SquaredCounter, (Counter, int, float)) = {issubclass(SquaredCounter, (Counter, int, float))}")
print(f"issubclass(Counter, (SquaredCounter, int, float)) = {issubclass(Counter, (SquaredCounter, int, float))}")

# isinstance() access tuple for comparing multiple classes
print(f"isinstance(c1, (Counter, int, float)) = {isinstance(c1, (Counter, int, float))}")
print(f"isinstance(c2, (Counter, int, float)) = {isinstance(c2, (Counter, int, float))}")
print(f"isinstance(c1, (SquaredCounter, int, float)) = {isinstance(c1, (SquaredCounter, int, float))}")
