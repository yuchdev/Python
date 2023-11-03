__doc__ = """Python hooks are used to implement custom behavior on some events.
It can replace metaclasses in most cases, as just another way of doing the same thing.

__init_subclass__ hook is called when a class is subclassed in the MRO order

As soon as you inherited from a class with __init_subclass__ hook,
it will be called on the subclass automatically
E.g. let's create class to check the coding style of the code to be PEP8 compliant (e.g. `variable_name`)
"""


class CodeStyleChecker:
    def __init_subclass__(cls, **kwargs):
        print(f"CodeStyleChecker.__init_subclass__({cls}, {kwargs})")
        super().__init_subclass__(**kwargs)

        # check we use only lower case letters and underscore
        for name in dir(cls):
            if name.startswith("__"):
                continue
            if not name.islower():
                raise ValueError(f"Invalid name: {name}")

    def __init__(self, **kwargs):
        print(f"CodeStyleChecker.__init__({self}, {kwargs})")
        super().__init__(**kwargs)


class MyClass(CodeStyleChecker):
    """
    Defining methods like `def IncorrectName(self)` will raise an exception
    """
    def __init__(self, a, b, **kwargs):
        super().__init__(**kwargs)
        self.a = a
        self.b = b

    def print_me(self):
        print(f"a == {self.a}, b == {self.b}")

    def __str__(self):
        return f"MyClass(a={self.a}, b={self.b})"


c = MyClass(10, 20)
print(f"c == {c}")
