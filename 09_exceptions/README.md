# Chapter 9. Exceptions

This chapter covers the philosophy of error handling, Python's exception hierarchy, the `try-except-else-finally` syntax, and context managers.

## Exception Philosophy
* **Stack Unwinding**: The process of searching for an exception handler by going up the call stack.
* **Exception Safety Levels**:
    1. **Nothrow**: The function is guaranteed not to throw exceptions.
    2. **Strong**: If an exception is thrown, the program state remains unchanged (rollback).
    3. **Basic**: If an exception is thrown, no resources are leaked and the state remains valid (though possibly changed).
* **Strategy**: Handle exceptions as close to the source as possible, or at clear "boundaries" (user input, thread, process).

## Exceptions in Python
* **Syntax**:
    ```python
    try:
        # Code that might raise an exception
    except ValueError as e:
        # Handle specific exception
    except (TypeError, KeyError):
        # Handle multiple exceptions
    else:
        # Run if NO exception was raised
    finally:
        # ALWAYS run (cleanup)
    ```
* **Raising**: Use `raise` to trigger an exception, or a bare `raise` inside an `except` block to re-raise the current exception.
* **Chaining**: Use `raise NewException from old_exception` to preserve context via the `__context__` and `__cause__` attributes.

## Custom Exceptions
Define your own exceptions by inheriting from the built-in `Exception` class. It's a best practice to create a base `Error` class for your module/library.

## Context Managers (`with` statement)
Context managers ensure resources (like files or database connections) are properly cleaned up.
* **Protocol**: Implement `__enter__` (setup) and `__exit__` (teardown).
* **`contextlib`**:
    * `@contextmanager`: Create a context manager using a generator.
    * `suppress(*exceptions)`: Ignore specific exceptions.
    * `ContextDecorator`: Allow a context manager to also be used as a decorator.

---
### Examples
* `01-theory.py`: Philosophy, stack unwinding, and `try-finally` vs `try-except`.
* `02-python.py`: Common built-in exceptions and `try-except-else-finally` blocks.
* `03-exception-api.py`: Chaining, `__context__`, and `__traceback__`.
* `04-multiple.py`: Handling multiple exceptions and custom exception hierarchies.
* `05-with.py`: Deep dive into `__enter__`/`__exit__` and `contextlib` utilities.
* `06-pdb.py`: Interactive debugging with `pdb.set_trace()`.
