# Chapter 2. Basic Collections

This chapter covers Python's built-in collection types: lists, tuples, sets, and dictionaries, along with their respective comprehensions.

## List (`list`)
Lists are mutable, ordered sequences of elements. They are implemented as arrays of pointers.
* **Creation**: `my_list = [1, 2, "Python"]` or `list(iterable)`.
* **Modification**: 
    * `append(x)`: Adds an item to the end.
    * `extend(iterable)`: Appends all items from an iterable.
    * `insert(i, x)`: Inserts an item at a given position.
    * `remove(x)`: Removes the first occurrence of `x`.
    * `pop([i])`: Removes and returns the item at index `i` (default last).
* **Slicing**: `my_list[start:stop:step]`.
* **Memory**: Loading a large list into memory can be expensive; consider generators for large datasets.

## Tuple (`tuple`)
Tuples are immutable, ordered sequences. They are generally faster than lists and can be used as dictionary keys if they contain only hashable elements.
* **Creation**: `my_tuple = (1, 2, 3)` or `single_item = (1,)`.
* **Unpacking**: `x, y, z = (1, 2, 3)`.
* **Nesting**: Tuples can contain mutable objects like lists, which can still be modified.

## Set (`set`)
Sets are unordered collections of unique, hashable elements. They are implemented as hash tables.
* **Creation**: `my_set = {1, 2, 3}` or `set(iterable)`. Note: `{}` creates an empty dictionary; use `set()` for an empty set.
* **Operations**:
    * `add(x)`, `update(iterable)`.
    * `remove(x)` (raises `KeyError` if missing) vs. `discard(x)` (does nothing if missing).
    * **Set Theory**: Union (`|`), Intersection (`&`), Difference (`-`), Symmetric Difference (`^`).

## Dictionary (`dict`)
Dictionaries are unordered (ordered by insertion since Python 3.7) mappings of unique keys to values.
* **Creation**: `my_dict = {"key": "value"}` or `dict(pairs)`.
* **Access**: `my_dict["key"]` or `my_dict.get("key", default)`.
* **Methods**: `keys()`, `values()`, `items()`, `update()`, `pop()`.
* **Inversion**: Can be inverted using `dict(zip(my_dict.values(), my_dict.keys()))`.

## Comprehensions
Comprehensions provide a concise way to create collections.
* **List Comprehension**: `[expr for item in iterable if condition]`.
* **Dict Comprehension**: `{key_expr: value_expr for item in iterable if condition]`.
* **Walrus Operator**: Can be used within comprehensions to assign values while evaluating: `[res for x in data if (res := process(x)) > 0]`.

---
### Examples
* `01-list.py`: List operations and memory notes.
* `02-dict.py`: Dictionary creation, access, and inversion.
* `03-list-comprehensions.py`: Advanced list mapping and filtering.
* `04-dict-comprehensions.py`: Dictionary mapping and key-value swapping.
* `05-set.py`: Set operations and mathematical sets.
* `06-tuple.py`: Immutability, unpacking, and indexing.
