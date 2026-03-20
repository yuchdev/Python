# Chapter 8. Classes

Python is an object-based language that supports full object-oriented programming. Everything in Python is an object, including classes themselves.

## Class Basics
* **Definition**: Classes are defined using the `class` keyword.
* **Initializer**: `__init__` is the initializer, not a constructor. The object is already created when `__init__` is called.
* **Attributes**: Created on the fly by assigning to `self`. There is no explicit declaration of members.
* **Methods**: Functions defined inside a class. The first argument is always `self`, representing the instance.

## Class vs. Instance Attributes
* **Instance Attributes**: Stored in `self.__dict__`. Unique to each instance.
* **Class Attributes**: Defined at the class level. Shared by all instances (similar to static members in other languages).
* **Attribute Lookup**: Python first looks in the instance `__dict__`, then in the class `__dict__`, and finally up the inheritance chain.

## Inheritance & Mixins
* **Single & Multiple Inheritance**: Python supports both.
* **MRO (Method Resolution Order)**: The order in which Python searches for methods in a class hierarchy. Accessible via `ClassName.mro()`.
* **Duck Typing**: "If it walks like a duck and quacks like a duck, it's a duck." Favor behavior over strict type checking.
* **Mixins**: Small classes designed to provide specific functionality to other classes through multiple inheritance.

## Properties & Managed Attributes
* **`@property`**: Turns a method into a "getter" that can be accessed like an attribute.
* **`__slots__`**: A list of allowed attribute names. Reduces memory usage by preventing the creation of `__dict__` for each instance.
* **Private Members**: Python uses a convention of a single underscore `_` for "internal" and double underscore `__` for name mangling to avoid name clashes in inheritance.

## Magic Methods (Dunder Methods)
Special methods surrounded by double underscores that allow objects to hook into Python's syntax:
* **Lifecycle**: `__init__`, `__new__`, `__del__`.
* **Representation**: `__str__` (informal), `__repr__` (official/debug).
* **Comparison**: `__eq__`, `__lt__`, `__le__`, etc. (Use `@functools.total_ordering` to simplify).
* **Arithmetic**: `__add__`, `__sub__`, `__mul__`, and their reflected versions (e.g., `__radd__`).
* **Containers**: `__len__`, `__getitem__`, `__setitem__`, `__contains__`.
* **Callable**: `__call__` allows an instance to be called like a function.

---
### Examples
* `01-basics.py`: Simple class definition and initializer.
* `02-attributes.py`: Class attributes and bound methods.
* `03-dict.py`: Exploring `__dict__` and dynamic attributes.
* `04-object.py`: Everything inherits from `object`.
* `05-properties.py`: Using `@property` for getters and setters.
* `06-slot.py`: Memory optimization with `__slots__`.
* `07-inheritance.py`: Basic inheritance and `super()`.
* `08-mangling.py`: Private attributes and name mangling.
* `09-multiple01.py` & `10-multiple02.py`: Multiple inheritance and MRO.
* `11-mixin.py`: Using mixins for reusable functionality.
* `12-magic.py`: Comprehensive guide to operator overloading.
