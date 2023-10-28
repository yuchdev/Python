__doc__ = """Python is a dynamically typed language, which means that the type of a variable is determined at runtime.
However, it also features meta classes, which can be used to change default behavior of classes.
Here's an example of a meta class that enforces strict typing of class attributes.
"""


class TypeCheckedAttribute:
    def __init__(self, expected_type, name):
        self.expected_type = expected_type
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Attribute '{self.name}' must be of type '{self.expected_type.__name__}'")
        instance.__dict__[self.name] = value


class StrictIntMeta(type):
    def __new__(cls, name, bases, dct):
        cls_instance = super().__new__(cls, name, bases, dct)
        for attr_name, attr_type in dct.get('__annotations__', {}).items():
            setattr(cls_instance, attr_name, TypeCheckedAttribute(attr_type, attr_name))
        return cls_instance


class StrictInt(metaclass=StrictIntMeta):
    def __init__(self, value: int):
        self.value = value


# Example usage with type hinting and variable assignment:
variable: StrictInt = 42
print(variable)

# This will raise a TypeError
variable = "42"
