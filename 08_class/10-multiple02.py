__doc__ = """Multiple inheritance in Python II
MRO stands for Method Resolution Order
super() calls the next class in MRO
Classes that come first in multiple inheritance come first in MRO
Classes that come lower in inheritance tree come later in MRO
First element if MRO is always the class itself, the last is 'object'
"""


class Base:
    def __init__(self, x=0):
        """
        """
        self.x = x

    def get(self) -> int:
        print("Base.get()")
        return self.x


class Left(Base):
    def __init__(self, x=0, y=0):
        """
        """
        super().__init__(x)
        self.y = y

    def get(self) -> int:
        print("Left.get()")
        return super().get()


class Right(Base):
    def __init__(self, x=0, z=0):
        """
        """
        super().__init__(x)
        self.z = z

    def get(self) -> int:
        print("Right.get()")
        return super().get()


class Child(Left, Right):
    pass


c = Child()
c.get()
# Left.get()
# Right.get()
# Base.get()
# super() is dynamic
# It's connected to MRO that stands for Method Resolution Order

# return tuple
print(f"MRO of Child: {Child.__mro__}")

# return list
print(f"MRO of Child: {Child.mro()}")


# How function super() can be actually implemented
def _super(cls, instance):
    """
    """
    class SuperProxy:
        """

        """
        def __init__(self, cls, obj):
            self.__cls = cls
            self.__instance = instance
            self.__obj = obj

        def __getattr__(self, item):
            """
            We redefine __getattr__ to call method of the wrapped object
            """
            method = getattr(super(cls, self._instance), item)
            if callable(method):
                return lambda *args, **kwargs: method(*args, **kwargs)
            else:
                return method

    mro = instance.__class__.mro()
    super_class = mro[mro.index(cls) + 1]
    # If we return class and not instance, we get an error
    # So we need to create a proxy object
    return SuperProxy(super_class, instance)
