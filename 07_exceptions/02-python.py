import sys

__doc__ = """Basics of exceptions in Python

* Python support arbitrary number of except clauses
* We may handle several exceptions in one except clause, passing them as a tuple

Hierarchy of exceptions:
    BaseException
        Exception
            ArithmeticError
                ZeroDivisionError
            LookupError
                IndexError
                KeyError
            TypeError
            ValueError
            RuntimeError
                NotImplementedError
            OSError
                FileNotFoundError
                PermissionError
            EOFError
            ImportError
            KeyboardInterrupt
            StopIteration
            GeneratorExit
            SystemExit
   
   
* except without any exception class will catch all exceptions. This considered bad practice
* use `except Exception` to catch all exceptions instead. Use it as a last handler
* catch everything is a bad practice, because it may catch exceptions that not intended to be caught, 
  e.g. KeyboardInterrupt
* Iteration plus mutation is a RuntimeError
* `raise` without any arguments will re-raise the last exception
* ImportError useful for dynamic imports, if one of the modules is not found we try to import another one
* AttributeError is raised when we try to access an attribute that does not exist, 
  or try to assign to an attribute that is read-only (e.g. slot) 
* IndexError is raised when we try to access an index that does not exist
* TypeError is raised when we try to access wrong type of dict key
* ValueError is raised when we pass wrong value as a key (including string to int conversion)

User-Defined Exceptions:
* User-defined exceptions should typically be derived from the Exception class,
* Making specific exception for library is a good practice
* Call it Error, because users will catch it as `except MyLibrary.Error`
"""

# Iteration plus mutation is a RuntimeError
try:
    dict_example = {1: 1, 2: 2, 3: 3}
    for key in dict_example:
        dict_example.pop(key)
except RuntimeError as e:
    print(f"RuntimeError: {e}")


# Python support arbitrary number of except clauses.
# We may handle several exceptions in one except clause, passing them as a tuple
# The syntax for this is:
try:
    print(f"Let's try to divide by zero 1 / 0={1 / 0}")
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")


# Subclasses of BaseException
print(f"f{BaseException.__subclasses__()}")

# Subclasses of Exception
print(f"f{Exception.__subclasses__()}")


# Hierarchy of User-Defined Exceptions
class Error(Exception):
    pass


class InputError(Error):
    pass


class DatabaseError(Error):
    pass

