# Chapter 13. Metaprogramming

Metaprogramming in Python allows you to write code that manipulates other code (classes and functions) at runtime. This chapter covers descriptors, managed attributes, and metaclasses.

## Descriptors
Descriptors are the mechanism behind `property`, `classmethod`, `staticmethod`, and even normal methods. A descriptor is an object that implements the **Descriptor Protocol**:
* `__get__(self, obj, type=None)`: Accessing the attribute.
* `__set__(self, obj, value)`: Setting the attribute.
* `__delete__(self, obj)`: Deleting the attribute.

### Types of Descriptors:
* **Data Descriptors**: Implement both `__get__` and `__set__`. They always take precedence over an instance's `__dict__`.
* **Non-Data Descriptors**: Implement only `__get__` (e.g., methods). They can be overridden by an entry in an instance's `__dict__`.

## Managed Attributes
* **`property`**: A built-in data descriptor that allows you to define getters, setters, and deleters as methods.
* **`classmethod` / `staticmethod`**: Non-data descriptors that change how a function is bound to a class or instance.

## Metaclasses
A metaclass is the "class of a class." It defines how a class itself is constructed.
* **`type`**: The default metaclass for all classes in Python.
* **Custom Metaclasses**: By inheriting from `type`, you can intercept class creation to enforce invariants, register classes, or modify attributes.
* **Metaclass Methods**:
    * `__prepare__`: Returns a mapping object to be used as the class namespace.
    * `__new__`: Responsible for creating and returning the new class object.
    * `__init__`: Initializes the newly created class object.
    * `__call__`: Called when you create an instance of the class (e.g., `MyClass()`).

---
### Examples
* `01-descriptors.py`: Implementing the descriptor protocol and attribute lookup order.
* `02-property.py`: Using `property` as a descriptor under the hood.
* `03-staticmethod.py`: How `staticmethod` and `classmethod` are implemented.
* `04-call.py`: Making objects callable with `__call__`.
* `05-meta.py`: Minimal metaclass and the `__prepare__`, `__new__`, `__init__` lifecycle.
* `06-strict.py`: A practical metaclass that enforces strict attribute definitions.
* `07-hooks.py`: Using `__init_subclass__` and other class creation hooks.
