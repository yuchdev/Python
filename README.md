# Python course

## Chapter 1.1. Native datatypes

### Module usage

* import path
* default attributes of empty module (`__name__`, `__module__`, etc.)

### Numeric

* boolean, integer, float, and complex
* numeric operations `+`, `-`, `*`, `**`, `/`, `//`
* `math.py`, `sys.maxint`

### String

* bytes string: `encode()`/`decode()`
* unicode string
* `r""` and `f""` forms

### List

* mutable, single types elements
* represented as list of pointers
* indexing and slicing

### Tuple

* immutable, different types elements
* could be dict key
* `(a,b,c) = x`

### Set and Dict

* Represented as hash table
* `keys()` return set
* `values()` and `items()` return list

### Files

* `open` and `with` statement
* `read()` - read all content
* `readlines()` - read all lines

### Comprehensions

#### List

* list comprehension provides a compact way of mapping a list into another list
* filesystem comprehension example
* `map()` and `filter()` functions
* combine a list comprehension with a sequence reduction
* we can perform database-like queries on sequences
* walrus operator allows you to run an expression while simultaneously assigning the output value
* matrix comprehension example
* list comprehension in Python works by loading the entire output list into memory
* it’s often helpful to use a generator instead of a list comprehension in Python

#### Dict

* dictionary comprehension similar to list comprehension, but it operates with key-value pairs
* swapping the keys and values of a dictionary example (value also must be hashable and unique)

## Chapter 2. Functions

### Function as object

* function objects has a number of attributes:
    * `__doc__` is the function’s documentation string
    * `__name__` is the function’s name
    * `__defaults__` is a tuple containing default argument values for those arguments that have defaults, or None if no
      arguments have a default value
    * `__code__` is the code object representing the compiled function body
    * `__globals__` is a reference to the dictionary that holds the function’s global variables — the global namespace of
      the module in which the function was defined
    * `__dict__` is the namespace supporting arbitrary function attributes
    * `__closure__` is None or a tuple of cells that contain bindings for the function’s free variables
    * `__annotations__` is a dictionary containing annotations of parameters
    * `__kwdefaults__` is a dictionary containing defaults for keyword-only parameters
    * `__call__` is a method that allows the function to be called
    * `__get__` is a method that returns a bound method object when the function is an instance attribute
* `id()` function returns an integer representing its identity
* Bytecode of function can be obtained by dis module

### Function arguments

* arguments is a tuple
* arguments can be passed by position or by keyword
* arguments can be empty
* you can Guarantee at least one argument by using *args
* arguments can have default values
* default values are evaluated at the point of function definition
* that's why you can't use mutable objects (e.g. set) as default values
* use `None` as default value and check it inside function
* arguments can be packed (while func definition) and unpacked (while calling)
* unpacking arguments as a list or dictionary
* `flatten()` example
* `keyargs()` example

### Function scope

* module functions are visible to all other functions in the module
    * Local scope: variables defined inside a function
    * Enclosing scope: variables defined inside a function, but used in a nested function
    * Global scope: variables defined outside a function
    * Builtin scope: variables preassigned in the builtin namespace
* you can define function with function
* inner function has access to outer function params. It is called 'closure'
* global variables can be used explicitly by using `global` keyword
* keyword `nonlocal` allows you to assign to variables in an outer (but non-global) scope
* you can use `dir()` function to get list of names in the current local scope
* you can use `globals()` and `locals()` functions to get dictionaries of global and local variables

### Lambda functions

* lambda functions are single-expression functions that are not necessarily bound to a name
* common syntax: `lambda argument_list: expression`
* lambda usecases:
  * sort key
  * filter
  * map/reduce
  * decorators
  * closures
  * currying

## Chapter 3. Decorators

* definition of decorator: a callable high-order function that takes a callable as input and returns another callable
* replacing __`name`__, __`doc`__, and __`module`__ of the decorator with respected values of the decorated function
* `functools.partial()` function allows you to create a new callable object with some of the arguments fixed
* `functools.wraps()` function is a decorator that copies the lost metadata from the undecorated callable to the
  decorator
* decorator with arguments examples: passing parameters, functions and streams
* examples of `init_once()` decorator and decorator that prevents calling function more than once with the same arguments
* example of deprecation decorator
* decorator that prevent calling function twice with the same arguments
* using decorators for debugging, logging and profiling

## Chapter 4. Input/Output

### Encoding

* examples of debug print decorators, from naive to production-ready
* history of encoding: ASCII, Unicode, UTF-8
* surrogate pairs and code points
* convert text to bytes and back
* escape sequences: Unicode, Hexadecimal, Octal, Binary, Raw, Unicode Database ID
* string normalization: NFC, NFD, NFKC, NFKD

### Filesystem

* `os` module
* file open modes: `r`, `w`, `a`, `x`, `b`, `t`, `+,` `U`
* `PYTHONUTF8` environment variable
* `read()` and `write()` methods
* `seek()` and `tell()` methods
* `readline()` and `readlines()` methods
* in-memory files: `io.StringIO` and `io.BytesIO`
* `with` statement

### String

* strings in Python are immutable sequences of Unicode code points
* character is simply a string of size one
* string literals can be enclosed in single quotes or double quotes
* formatting strings with `format()` method
* formatting strings with f-strings
* formatting string alignment, padding, truncation, and more
* formatting numbers with `format()` method: decimal, binary, octal, hexadecimal, scientific, percentage, currency
* parsing strings with `split()` and `join()` methods
* object string representation with `__repr__()` and `__str__()` methods
* string case conversion with `upper()`, `lower()`, `capitalize()`, `title()`, `swapcase()` methods

## Chapter 5. Collections

* thread-safe queues: `queue.Queue`, `queue.LifoQueue`
* deque: `collections.deque`
* priority queue: `heapq`, `queue.PriorityQueue`
* tuples: `collections.namedtuple`, `collections.Counter`
* dictionaries: `collections.defaultdict`, `collections.OrderedDict`, `collections.ChainMap`

## Chapter 6. Classes

### Class Definition

* classes were introduced in Python 2.2
* Python is not object-oriented language, but rather object-based
* class is a blueprint for creating objects
* in Python `__init__()` is not a constructor, but rather initializer
* Python class members don't have declaration
* Python class members are public by default

### Class Attributes

* class attributes are shared by all instances of the class
* analogy to static members in C++ and Java
* no explicit declaration of attributes in `__init__()` is required
* access class attributes from instances and from the class itself
* bound methods is a special case of attributes that are callable

### Class Dictionary

* class members are actually stored in class dictionary called `__dict__`
* you can access them directly by using `MyClass.__dict__` attribute
* function `vars()` returns a dict of local variables
* you can add and remove attributes on the fly using `__dict__`

### Class as Object

* class duality in Python: class is an object and class is a statement
* class is also a statement, so it can be used in expressions
* class can be passed as an argument to a function and returned from a function
* class can be assigned to a variable

### Class Properties

* property is a special kind of attribute that has a getter and a setter
* property is a method that uses `@property` decorator
* resulting object is called descriptor, which behaves like a data field
* property can be used to implement read-only attributes
* process of choosing the best data representation in Python is following:
  * never use getter/setter like in C++/Java
  * use public attributes if you don't have invariant
  * use properties if you have invariant and read-only attributes
  * use `__slots__` if you have a lot of objects
  * use `__getattr__()` and `__setattr__()` if you want to implement dynamic attributes
  * use `dict`/`NamedTuple` if you have a lot of attributes
  * finally, use method is you have side-effects, a lot of code, or you need to pass arguments

### Slots

* `__slots__` is a class attribute that defines a list of allowed attributes
* it is useful for performance reasons, as it saves memory
* you can't have both `__dict__` and `__slots__` in the same class
* `__slots__` is a tuple of strings, which are names of class members
* attempt to assign to an unlisted attribute raises `AttributeError`

### Inheritance

* inheritance is a mechanism for code reuse
* Python works as duck-typing language. Do not use inheritance unless required
* `isinstance()` is a way to check if object is an instance of a class
* `issubclass()` is a way to check if class is a subclass of another class
* there's no such thing as private members in Python, however you can use name mangling
* according to agreement, members start with `_` are private nd visible, abd with `__` are private and mangled
* Python allows multiple inheritance
* lookup order is called MRO (method resolution order)
* classes that come first in multiple inheritance come first in MRO
* classes that come lower in inheritance tree come later in MRO
* first element if MRO is always the class itself, the last is `object`
* mixin is a class that is used to add functionality to other classes

## "Magic" methods

* comparison: `__lt__`, `__le__`, `__eq__`, `__ne__`, `__gt__`, `__ge__`
* arithmetic: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, `__matmul__
* augmented assignment: `__iadd__`, `__isub__`, `__imul__`, `__itruediv__`, `__ifloordiv__`, `__imod__`, `__ipow__`,
  `__imatmul__`
* unary: `__neg__`, `__pos__`, `__abs__`, `__invert__`
* type conversion: `__int__`, `__float__`, `__complex__`, `__bool__`, `__bytes__`, `__str__`, `__repr__`, `__format__`
* container: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, `__contains__`
* context manager: `__enter__`, `__exit__`
* attribute access: `__getattr__`, `__setattr__`, `__delattr__`, `__getattribute__`
* callable: `__call__`
* iterator: `__iter__`, `__next__`
* async iterator: `__aiter__`, `__anext__`
* async context manager: `__aenter__`, `__aexit__`
* async callable: `__acall__`


## Chapter 7. Exceptions

### Exception Theory

* process of exception handling includes stack unwinding
* error handling facts in general, not only in Python:
  * 92% of catastrophic errors in complex systems are due to wrong error handling
  * error handling is more complex than handling of normal cases
  * testing of error handling is more difficult than testing of normal cases
  * error handling is often not tested at all
* there are 2 interesting techniques for error handling:
  * make as many error case impossible or make them normal cases (e.g. restore db from backup every day)
  * crash-only software: if something goes wrong, crash the system and restart it
* what could be considered as an error?
  * errors due to wrong input or other runtime errors
  * errors due to wrong usage of the system
  * errors due to system failures
  * error due to communication failures
* example with opening file in command-line application and GUI application
* we are losing information about the context of the exception while unwinding the stack
* handle exceptions as close to the place where they were raised as possible
* 3 levels of exception safety:
  * basic guarantee: no resources are leaked, but the program state may be corrupted
  * strong guarantee: no resources are leaked and the program state is unchanged
  * nothrow guarantee: no exceptions are thrown
* possible exception boundaries:
  * process boundary: between processes
  * thread boundary: between threads
  * module boundary: between modules
  * class boundary: between classes
  * function boundary: between functions

### Exceptions in Python

* exception handling in Python is quite simple, based of try-except-finally for handling
* raise is used to raise an exception
* one more approach is to exclude except blocks and use only try-finally blocks
* Python support arbitrary number of except clauses
* we may handle several exceptions in one except clause, passing them as a tuple
* `except` without any exception class will catch all exceptions. This considered bad practice
* use `except Exception` to catch all exceptions instead
* `raise` without any arguments will re-raise the last exception
* `ImportError` useful for dynamic imports, if one of the modules is not found we try to import another one
* `AttributeError` is raised when we try to access an attribute that does not exist, or try to assign to a read-only
  attribute
* `KeyError` is raised when we try to access a dictionary key that does not exist
* `IndexError` is raised when we try to access a list or tuple element that does not exist
* `TypeError` is raised when we try to call a function with wrong number of arguments or wrong argument types

### User-defined Exceptions

* you can define your own exception classes by inheriting from `Exception` class
* making specific exception for library is a good practice
* call it `Error`, because users will catch it as `except MyLibrary.Error`
* it's a good practice to define your own exception hierarchy

### Exception API

* you can pass any number of arguments to `Exception` constructor
* you can access exception arguments via `Exception.args` attribute.
  You can use it for passing additional information to the handler
* you can access exception traceback via `Exception.__traceback__` attribute
  This allows passing entire exception context to the handler
* you can access exception type via `Exception.__class__` attribute
  This is how you can check exception type in except block
* Traceback is being created only if exception is being raised
  It is None on `Exception.__init__` call, and initialized on raise
* Traceback filled with information dynamically in the moment of passing stack layers
* Methods `__str__()` and `__repr__()` are being called on exception printing
  They are usually not very informative
* In order to get more information about exception you can use traceback module
* You can use `traceback.format_exc()` to print exception
* You can use `traceback.print_tb()` to print exception traceback to stdout
* In Python you can throw and handle multiple exceptions
* You can wrap one exception into another
* `Exception.__context__` attribute contains exception that was raised before
* 4 forms of raise:
  * raise exception without context: `raise Exception`
  * old_exception is being saved in __context__: `raise Exception("message") from old_exception`
  * no cause: `raise Exception("message") from None`  
  * re-raise exception with context: `raise` 
* `try` can contain `else` block, it is used for code that should be executed only if no exception was raised

### Context Managers

* when you need to handle multiple resources straightforward way may not work as expected
* use `with` statement to handle multiple resources
* `with` statement is a syntactic sugar for `try-finally` block
* it releases resources automatically in an order reverse to opening
* `__enter__` method is called when 'with' statement is executed
* `__exit__` method is called when 'with' statement is finished
* parameters can be replaced with `*exc_info`
* Don't forget to add the check for double release
* `contextlib` contains class `AbstractContextManager` that can be used as a base class for context managers
  and provides default implementation of `__enter__` and `__exit__` methods
* examples of context managers in standard library:
  * `cd` - change directory and return to the previous one
  * `tempfile.TemporaryFile` - create temporary file and remove it when 'with' statement is finished
  * `contextlib.suppress` - suppress exceptions of given type
  * `contextlib.redirect_stdout` - redirect stdout to given file
  * `contextlib.ContextDecorator` - base class that can be used to define context managers

### Logging and Debugging

* Python's `logging` module is helpful for logging error messages and debugging information
* the `pdb` module provides a built-in debugger for tracing errors and debugging code interactively
* `pdb.set_trace()` enters debugger interactive mode

## Chapter 8. Iterators

TBC
