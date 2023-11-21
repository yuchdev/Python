class Counter:
    """
    I'm counter, I count stuff
    """
    # Class attributes are shared by all instances of a class
    # It's an analogy to static variables in C++
    all_counters = []

    def __init__(self, start=0):
        """
        No explicit declaration of attributes
        """
        self.counter = start
        self.all_counters.append(self)

    def get(self) -> int:
        return self.counter

    def increment(self):
        self.counter += 1


# Class members are actually elements of a dict
# You can access them directly
print(f"Counter.__dict__ = {Counter.__dict__}")
assert Counter.__dict__['all_counters'] is Counter.all_counters

# Function vars() returns a dict of local variables
print(f"vars() = {vars()}")

# You can add and remove attributes on the fly using __dict__
Counter.__dict__['new_attribute'] = 42

# noinspection PyUnresolvedReferences
print(f"Counter.new_attribute = {Counter.new_attribute}")
print("Delete Counter.new_attribute")
del Counter.__dict__['new_attribute']

# You can also use setattr() and getattr()
setattr(Counter, 'new_attribute2', 43)

# noinspection PyUnresolvedReferences
print(f"Counter.new_attribute2 = {getattr(Counter, 'new_attribute2')}")
print("Delete Counter.new_attribute2")
delattr(Counter, 'new_attribute2')
