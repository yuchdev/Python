# Chapter 1. Native Datatypes

This chapter covers the fundamental data types in Python: numeric types, strings, booleans, `None`, and basic file I/O. Python is a dynamically typed language, but it is also strongly typed.

## Module Attributes
Even an "empty" module in Python has several implicit attributes:
* `__name__`: The name of the module. If the module is being run directly, this is set to `"__main__"`.
* `__doc__`: The docstring of the module.
* `__package__`: The package the module belongs to.
* `__file__`: The path to the module file.

## Numeric Types
Python supports several numeric types:
* **Integers (`int`)**: Can be arbitrarily large, limited only by available memory.
* **Floats (`float`)**: Double-precision floating point numbers.
* **Complex (`complex`)**: Numbers with real and imaginary parts (e.g., `2 + 7j`).
* **Fractions (`fractions.Fraction`)**: Rational numbers represented as a numerator and denominator.

### Key Operations & Concepts:
* **Arithmetic**: `+`, `-`, `*`, `**` (power), `/` (float division), `//` (floor division), `%` (modulo).
* **Floor Division (`//`)**: For positive numbers, it truncates. For negative numbers, it rounds towards negative infinity.
* **Walrus Operator (`:=`)**: Assigns a value to a variable as part of an expression.
* **Type Checking**: Use `type(x)` to get the type or `isinstance(x, int)` for boolean checks.
* **Constants**: `math.pi`, `math.e`, `float("inf")`, `float("nan")`.

## Strings (`str`)
Strings are immutable sequences of Unicode code points.
* **Literals**: Created with `' '`, `" "`, or `''' '''`/`""" """` for multiline strings.
* **Prefixes**: 
    * `r"..."`: Raw strings (ignores escape sequences, useful for regex/paths).
    * `f"..."`: F-strings (formatted string literals).
* **Methods**: `upper()`, `lower()`, `find()`, `replace()`, `split()`, `join()`.
* **Slicing**: `s[start:stop:step]`. Supports negative indexing (e.g., `s[-1]` is the last character).

## Booleans & None
### Boolean (`bool`)
* Values: `True` and `False`.
* Subclass of `int`: `True == 1`, `False == 0`.
* **Falsy values**: `None`, `0`, `0.0`, `""`, `[]`, `()`, `{}`, `set()`.

### None Type
* `None` is a singleton representing the absence of a value.
* Often used as a default return value or for initializing variables.

## Basic File I/O
* **Opening**: `open(filename, mode)` where mode can be `'r'` (read), `'w'` (write), `'a'` (append), etc.
* **Context Manager**: Using `with open(...) as f:` ensures the file is closed automatically.
* **Methods**:
    * `read()`: Reads the entire file content.
    * `readlines()`: Reads all lines into a list.
    * `readline()`: Reads a single line.

---
### Examples
* `01-empty-module.py`: Demonstrates module reflection.
* `02-numeric-types.py`: Numeric operations, fractions, and walrus operator.
* `03-string-type.py`: String manipulation, indexing, and formatting.
* `04-boolean-none.py`: Boolean logic and `None` type.
