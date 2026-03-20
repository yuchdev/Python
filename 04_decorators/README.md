# Chapter 4. Decorators

A decorator is a higher-order function that takes another function as an argument and returns a new function, usually adding some functionality to the original one without permanently modifying it.

## Anatomy of a Decorator
A basic decorator typically looks like this:
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
```

### Preserving Metadata
When you decorate a function, it technically becomes the `wrapper` function, losing its original `__name__`, `__doc__`, and other attributes. To fix this, use `functools.wraps`:
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## Advanced Decorators
* **Decorators with Arguments**: To pass arguments to the decorator itself, you need another layer of nesting (a decorator factory).
* **Stateful Decorators**: Decorators can maintain state using function attributes or closures (e.g., a `call_once` decorator).
* **Memoization**: Caching the results of expensive function calls based on their arguments (e.g., `functools.lru_cache`).
* **Single Dispatch**: `functools.singledispatch` allows for simple function overloading based on the type of the first argument.

## Common Use Cases
* **Logging & Debugging**: Printing function calls, arguments, and return values.
* **Profiling**: Measuring the execution time of a function.
* **Access Control**: Checking permissions before executing a function.
* **Initialization**: Ensuring a function (like a database connection) is only called once.

---
### Examples
* `01-debug-print.py`: Evolution of a debug decorator from naive to using `wraps`.
* `02-initialize.py`: Implementing `call_once` to ensure single execution.
* `03-deprecated.py`: A decorator to mark functions as deprecated.
* `04-profile.py`: Timing functions, manual memoization, `lru_cache`, and `singledispatch`.
