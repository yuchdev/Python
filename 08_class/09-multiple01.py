__doc__ = """Multiple inheritance in Python
"""


class LeftBase:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get(self) -> int:
        print("LeftBase.get()")
        return self.x


class RightBase:
    def __init__(self, x=0, z=0):
        self.x = x
        self.z = z

    def get(self) -> int:
        print("RightBase.get()")
        return self.z


class Child(LeftBase, RightBase):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z


child = Child(1, 2, 3)
print(f"child.get() = {child.get()}")
print(f"child.get() = {child.get()}")
# Called LeftBase.get(), no matter how many times we call child.get()
# Lookup order is LeftBase, RightBase, Child
# When the argument is found, we return it and never looking further


