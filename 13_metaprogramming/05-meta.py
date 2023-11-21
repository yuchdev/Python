__doc__ = """In Python we can use meta-programming to create classes and functions dynamically.
By default, Python uses `type` metaclass to create classes.
It can be changed by specifying `metaclass` keyword argument in the class definition.

Usually metaclass is derived from `type` metaclass, but technically it's not necessary.
Metaclass must provide `__call__` method, which is called when the class is instantiated.
On this place can be any callable, e.g. function, class, lambda, etc.

Method `__prepare__` is called before `__new__` and `__init__`
It must return a mapping object that will be used as a namespace for the class.

Useful metaclasses:
* `abc.ABCMeta` - abstract base classes
* Iterable - `collections.abc.Iterable` throws an exception if `__iter__` is not implemented
"""

import abc


class Base:
    pass


# noinspection PyUnresolvedReferences
class UseMetaLambda(Base, var=92, metaclass=lambda *args, **kwargs: print(f"meta({args}, {kwargs})")):
    """
    Pass lambda object as a metaclass
    It's enough as it's just another callable
    It prints: class name, base classes, keyword arguments, etc.
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_me(self):
        print(f"a == {self.a}, b == {self.b}")


# Don't create instance of this class, it won't work
# print() as a metaclass is not a good idea, because it returns None
# However class declaration itself is enough to call metaclass


# noinspection PyUnresolvedReferences
class Meta(type):
    """
    Typical metaclass implementing `__call__`, `__new__` and `__prepare__` methods
    """

    def __new__(mcs, name, bases, namespace, **kwargs):
        """
        :param mcs: metaclass
        :param name: name of the class
        :param bases: base classes
        :param namespace: namespace of the class
        :param kwargs: keyword arguments
        :return: new instance of the class
        """
        print(f"Meta.__new__({mcs}, {name}, {bases}, {namespace}, {kwargs})")
        return super().__new__(mcs, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        """
        `__init__` can be compared to "decorator" of metaclass, because
        it's called after the class is created, but before it's returned as a result
        in order to modify the behavior
        :param cls: class
        :param name: name of the class
        :param bases: base classes
        :param namespace: namespace of the class
        :param kwargs: keyword arguments
        """
        print(f"Meta.__init__({cls}, {name}, {bases}, {namespace}, {kwargs})")
        super().__init__(name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        """
        Before Python 3.7. it specified the namespace of the class as an OrderedDict.
        After 3.7 dict is ordered by default, so it's not necessary anymore.
        :param mcs: metaclass
        :param name: name of the class
        :param bases: base classes
        :param kwargs: keyword arguments
        :return: mapping object that will be used as a namespace for the class
        """
        print(f"Meta.__prepare__({mcs}, {name}, {bases}, {kwargs})")
        return super().__prepare__(name, bases)

    def __call__(cls, *args, **kwargs):
        """
        :param cls: class
        :param args: arguments to be passed to the constructor of the class
        :param kwargs: keyword arguments to be passed to the constructor of the class
        :return: instance of the class
        """
        print(f"Meta.__call__({cls}, {args}, {kwargs})")
        obj = cls.__new__(cls, *args, **kwargs)


# noinspection PyUnresolvedReferences
class Iterable(metaclass=abc.ABCMeta):
    """
    Metaclass is used to check that the class implements `__iter__` method
    You also can check method signature using `inspect.signature` module
    """
    @abc.abstractmethod
    def __iter__(self):
        raise NotImplementedError()
