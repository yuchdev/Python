# Chapter 10. Iterators & Generators

This chapter explores Python's iteration protocol, lazy evaluation with generators, and bidirectional communication with coroutines.

## Iteration Protocol
In Python, iteration is powered by two methods:
1. **`__iter__()`**: Returns an iterator object.
2. **`__next__()`**: Returns the next value or raises `StopIteration` when exhausted.

* **Iterable**: An object that implements `__iter__`.
* **Iterator**: An object that implements both `__iter__` and `__next__`. (An iterator is always an iterable that returns itself).

## Generators
Generators are functions that use the `yield` keyword. They allow you to produce a sequence of values lazily, saving memory.
* **Lazy Evaluation**: Values are computed only when requested.
* **State Preservation**: The generator's local variables and execution state are "paused" at `yield` and "resumed" on the next call.
* **Generator Expressions**: Concise, parenthesized syntax for creating generators: `(x*x for x in range(10))`.

## `itertools` Module
A collection of tools for efficient iteration:
* **`chain(*iterables)`**: Combines multiple iterables into one.
* **`count(start, step)`**: An infinite arithmetic progression.
* **`cycle(iterable)`**: Repeats an iterable indefinitely.
* **`islice(iterable, start, stop, step)`**: Slices an iterator.

## Coroutines (Generator-based)
By using `yield` as an expression (`value = yield`), generators can consume data sent to them via the `send()` method.
* **Bidirectional**: Data can flow both out of (yield) and into (send) the generator.
* **States**: Coroutines can be used to implement finite state machines.
* **Note**: Modern Python uses `async def` for asynchronous coroutines, but generator-based coroutines are the foundation.

---
### Examples
* `01-protocol.py`: Implementing custom `Iterable` and `Iterator` classes.
* `02-iterable.py`: Differences between iterables and iterators.
* `03-generators.py`: Generator functions, infinite streams, and pipelines.
* `04-tree.py`: Recursive tree traversal using `yield from`.
* `05-expressions.py`: Memory comparison between list comprehensions and generator expressions.
* `06-itertools.py`: Practical usage of the `itertools` library.
* `07-io.py`: Lazy file reading using iterators.
* `08-with.py`: Combining context managers and generators (`ExitStack`).
* `09-coroutines.py`: Using `yield` to receive data with `send()`.
