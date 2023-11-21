__doc__ = """Let's emulate @property decorator using metaprogramming
"""


class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def __repr__(self):
        return f"Temperature(celsius={self.celsius})"

    def __str__(self):
        return f"{self.celsius}°C"


t = Temperature(30)
print(f"t is {t}")
print(f"t.fahrenheit is {t.fahrenheit}")

t.fahrenheit = 86
print(f"t is {t}")
print(f"t.fahrenheit is {t.fahrenheit}")

assert t.celsius == 30


# noinspection PyPep8Naming
class custom_property:
    def __init__(self, function_get, function_set=None, function_del=None):
        """
        Create a custom property decorator object
        :param function_get: function to be used for getting an attribute value
        :param function_set: function to be used for setting an attribute value
        :param function_del: function to be used for deleting an attribute value
        """
        self.function_get = function_get
        self.function_set = function_set
        self.function_del = function_del

    def __get__(self, obj, cls):
        """
        :param obj: instance of the class
        :param cls: type of the instance
        :return:
        """
        if obj is None:
            return self
        if self.function_get is None:
            raise AttributeError("unreadable attribute")
        return self.function_get(obj)

    def __set__(self, obj, value):
        if self.function_set is None:
            raise AttributeError("can't set attribute")
        self.function_set(obj, value)

    def __delete__(self, obj):
        if self.function_del is None:
            raise AttributeError("can't delete attribute")
        self.function_del(obj)

    def getter(self, function_get):
        """
        Return a new custom property decorator object with the same function_set and function_del
        """
        return type(self)(function_get, self.function_set, self.function_del)

    def setter(self, function_set):
        """
        Return a new custom property decorator object with the same function_get and function_del
        """
        return type(self)(self.function_get, function_set, self.function_del)

    def deleter(self, function_del):
        """
        Return a new custom property decorator object with the same function_get and function_set
        """
        return type(self)(self.function_get, self.function_set, function_del)


class Temperature2:
    def __init__(self, celsius):
        self.celsius = celsius

    @custom_property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9

    def __repr__(self):
        return f"Temperature(celsius={self.celsius})"

    def __str__(self):
        return f"{self.celsius}°C"


t = Temperature2(30)
print(f"t is {t}")
# noinspection PyPropertyAccess
print(f"t.fahrenheit is {t.fahrenheit}")

t.fahrenheit = 86
print(f"t is {t}")
# noinspection PyPropertyAccess
print(f"t.fahrenheit is {t.fahrenheit}")
assert t.celsius == 30
