# Python for Developers

## Chapter 1. Native datatypes

### Module usage

* `import path`
* default attributes of empty module (`__name__`, `__module__`, etc.)

### Numeric

* boolean, integer, float, and complex
* numeric operations `+`, `-`, `*`, `**`, `/`, `//`
* `math.py`, `sys.maxint`

### String

* bytes string: `encode()`/`decode()`
* unicode string
* `r""` and `f""` forms

### Files

* `open` and `with` statement
* `read()` - read all content
* `readlines()` - read all lines

### Chapter 2. Basic Collections

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

#### List Comprehensions

* list comprehension provides a compact way of mapping a list into another list
* filesystem comprehension example
* `map()` and `filter()` functions
* combine a list comprehension with a sequence reduction
* we can perform database-like queries on sequences
* walrus operator allows you to run an expression while simultaneously assigning the output value
* matrix comprehension example
* list comprehension in Python works by loading the entire output list into memory
* it’s often helpful to use a generator instead of a list comprehension in Python

#### Dict Comprehensions

* dictionary comprehension similar to list comprehension, but it operates with key-value pairs
* swapping the keys and values of a dictionary example (value also must be hashable and unique)

## Chapter 3. Functions

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

## Chapter 4. Decorators

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

## Chapter 5. Regular Expressions

This chapter focuses on Python-specific usage of regular expressions via the standard re module. It complements prior knowledge of regex syntax by emphasizing Python APIs, Unicode handling, bytes vs str, performance, and common patterns.

### Goals

- Understand Python's re module objects: Pattern and Match
- Choose the right function: match, fullmatch, search, findall, finditer, split, sub, subn
- Use grouping: numbered, named, non-capturing, backreferences
- Learn and combine flags: IGNORECASE, MULTILINE, DOTALL, ASCII, VERBOSE, etc.
- Work correctly with Unicode and bytes
- Apply practical text-processing tasks idiomatically in Python
- Recognize performance pitfalls and mitigation strategies

### Theory (as in Python docs)

- Module re overview and compilation
  - re.compile(pattern, flags=0) returns Pattern
  - Pattern methods vs module-level functions
  - Raw string literals r"..." and escaping in Python strings
- Matching primitives
  - match vs fullmatch vs search
  - findall vs finditer (lists vs iterators, groups result shapes)
  - split and maxsplit; capturing groups in split
  - sub vs subn; callable replacement function signature (def repl(m: Match) -> str)
- Groups and references
  - Capturing groups ( ... ), non-capturing (?: ... ), named groups (?P<name>...)
  - Access: m.group(), m.groups(), m.groupdict(), m["name"], m.start(), m.end(), m.span()
  - Backreferences: \1, (?P=name)
- Flags
  - re.IGNORECASE, re.MULTILINE, re.DOTALL, re.ASCII, re.VERBOSE, re.DEBUG
  - Combining flags with |; flags on compile and inline (?i), (?m), (?s), (?x)
- Lookaround
  - Lookahead (?=...) (?!...), lookbehind (?<=...) (?<!...)
  - Python lookbehind is fixed-width
- Unicode and locales
  - Default behavior is Unicode-aware; \w, \b, casefolding nuances with IGNORECASE
  - re.ASCII to restrict \w, \d, \s to ASCII
  - Normalization note: use unicodedata.normalize before regex when equivalence matters
- Bytes vs str
  - Pattern and input types must match (both bytes or both str)
  - Flags behavior with bytes (e.g., re.ASCII implied for classes)
- Performance and safety
  - Pre-compile patterns used in loops
  - Prefer specific patterns; avoid catastrophic backtracking patterns
  - Use finditer for large inputs; lazy quantifiers when appropriate
  - Python 3.11+ supports timeout= on many APIs; otherwise watchdogs

### Practical examples (scripts in 05_regex)

- 01-basics.py — quick tour: compile, search, findall, sub; greedy vs non-greedy; lookarounds
- 02-match-search-fullmatch.py — differences and typical use-cases
- 03-groups-named.py — capturing, named groups, backreferences, Match API
- 04-flags-verbose.py — flags combinations, multiline, dotall, verbose with comments
- 05-finditer-split-sub.py — finditer memory-friendly scans; split with captures; sub and subn with callable
- 06-unicode-and-bytes.py — Unicode categories, normalization, bytes patterns
- 07-performance.py — compilation in loops, benchmarking patterns, notes on timeout (if 3.11+)

### Suggested exercises

- Validate and parse log lines (datetime, level, message) with named groups
- Normalize phone numbers with sub + callable
- Tokenize CSV-like lines handling quoted fields (lookarounds or a balanced approach)
- Extract hashtags and @mentions from text (Unicode word chars) with tests for ASCII vs Unicode
- Write a URL highlighter using finditer and spans to wrap matches
- Benchmark two alternative patterns on a large text and compare runtimes

## Chapter 6. Input/Output

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

## Chapter 7. Additional Collections

* thread-safe queues: `queue.Queue`, `queue.LifoQueue`
* deque: `collections.deque`
* priority queue: `heapq`, `queue.PriorityQueue`
* tuples: `collections.namedtuple`, `collections.Counter`
* dictionaries: `collections.defaultdict`, `collections.OrderedDict`, `collections.ChainMap`

## Chapter 8. Classes

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


## Chapter 9. Exceptions

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

## Chapter 10. Iterators and Generators

TBC

## Chapter 11. Asynchronous Programming

This chapter covers Python's asynchronous subsystem built around coroutines, the event loop, tasks, and async I/O. You will connect prior topics (Exceptions, Iterators/Generators, Context Managers, OOP) to write robust, concurrent I/O-bound programs.

### Goals

- Understand async/await syntax, coroutines, and the event loop
- Create and manage Tasks; coordinate with gather, as_completed, and shields
- Handle cancellation, timeouts, and exception propagation in async code
- Use async iterators, async generators, and async context managers
- Compare threading, multiprocessing, and asyncio for I/O vs CPU workloads
- Build small TCP clients/servers with asyncio streams

### Theory (as in Python docs)

- Coroutines and awaitables
  - async def, await; coroutine lifecycle; Task vs bare coroutine
  - Event loop responsibilities; scheduling and cooperative multitasking
- Task orchestration
  - asyncio.create_task, gather, wait, as_completed
  - Shields and cancellation semantics (CancelledError), timeout helpers
- Async context managers and iterators
  - __aenter__/__aexit__, __aiter__/__anext__
  - Using async with and async for
- Exceptions in async code
  - How exceptions propagate from tasks; TaskGroup (3.11+) overview
  - Aggregating exceptions; handling partial failures
- Networking primitives
  - asyncio streams (open_connection, start_server), protocols/transports
- When to pick what
  - Threads for blocking I/O, asyncio for many sockets, processes for CPU-bound

### Practical examples (scripts in 11_async)

- 01-rocket-example.py — simple demo of concurrent coroutines and delays
- 02-state-machine.py / 03-state-machine.py — modeling async workflows
- 04-async.py / 05-async.py — basic async/await, tasks, gather
- 06-net-client.py — TCP client using asyncio streams
- 07-net-server.py — simple echo server
- 08-async-server.py / 09-async-server2.py — progressively improved async servers

## Chapter 12. Performance in Python

This chapter focuses on measuring, understanding, and improving performance in Python, with emphasis on correct measurement, algorithmic choices, memory behavior, concurrency trade-offs, and Python-specific optimizations. It intentionally builds on OOP (object layout, __slots__), Iterators/Generators (lazy evaluation), Async subsystem (I/O concurrency), and Exceptions (cost and control flow patterns).

### Goals

- Measure performance correctly (time and memory) and find hotspots with profilers
- Choose appropriate algorithms and data structures for time and space
- Use iterators/generators and streaming I/O to reduce memory pressure
- Apply caching/memoization and understand trade-offs
- Understand the GIL and pick the right concurrency model for CPU vs I/O
- Recognize when to use vectorized/native code (builtins, C-extensions, NumPy)

### Theory (as in Python docs)

- Measurement tools
  - timeit vs time.perf_counter; statistical considerations; warmups
  - Profilers: cProfile + pstats; function-level vs line-level idea; tracing overhead
  - Basic memory observation: sys.getsizeof, tracemalloc overview
- Data structures and algorithms
  - Big-O intuition; constant factors in Python
  - Lists vs tuples; dict/set membership; heaps and priority queues (heapq)
  - OOP cost: attribute lookup, __dict__ vs __slots__
- Iterators, generators, and streaming
  - Generator functions and expressions; lazy pipelines with itertools
  - I/O streaming patterns; avoiding loading whole files
- Exceptions and control flow
  - Cost of exceptions; EAFP vs LBYL; balancing readability and speed
- Caching
  - functools.lru_cache and manual caches; invalidation; memory vs speed
- Concurrency and GIL
  - GIL implications; threads for I/O, multiprocessing for CPU, asyncio for many sockets
  - Using concurrent.futures; process pools vs thread pools
- Free-threaded CPython (Python 3.13, experimental)
  - PEP 703 introduces a build of CPython without the GIL. Availability and flags (e.g., `-X gil=0`) depend on your build.
  - New atomic primitives (atomic module) provide lock-free operations; API is experimental and may change.
  - CPU-bound threads can scale on multi-core only in a free-threaded build; otherwise prefer multiprocessing.
  - Use with caution: third-party C extensions may not yet be compatible; measure and validate correctness.
- Native speed paths
  - Builtins and comprehensions; vectorization via NumPy; Cython/Extension overview; PyPy note

### Practical examples (scripts in 12_performance)

- 01-basics.py — small timing demo, builtins vs Python loops, __slots__ note
- 02-timeit-perf_counter.py — micro-benchmarking pitfalls and usage
- 03-cprofile.py — profiling a synthetic workload and reading stats
- 04-algorithms-data-structures.py — list vs set membership, dict lookups, heapq
- 05-generators-vs-lists.py — memory and throughput trade-offs for generators
- 06-caching-memoization.py — @lru_cache on expensive functions
- 07-async-io-vs-threads.py — I/O-bound concurrency comparison (asyncio vs threads)
- 08-multiprocessing.py — CPU-bound work with ProcessPoolExecutor
- 09-free-threaded-threads.py — CPU-bound threads on free-threaded CPython 3.13 (experimental) with atomic demo

### Suggested exercises

- Profile a text-processing pipeline; eliminate the top two hotspots without changing external behavior
- Replace list-based processing with generators; measure memory improvement on large inputs
- Implement caching for a pure function; compare cold vs warm timings; discuss invalidation
- Rewrite a membership-heavy workload using sets/dicts; show speedups
- Compare asyncio.gather vs ThreadPoolExecutor for simulated I/O tasks

## Chapter 13. Metaclasses

This chapter explores Python's metaprogramming toolkit: descriptors, function-to-attribute adapters (property/staticmethod), callable objects, and metaclasses. You will connect concepts from Classes and Decorators to control class creation and behavior.

### Goals

- Understand descriptors and how they power property and other managed attributes
- Use property, staticmethod, and classmethod appropriately
- Write callable objects (__call__) and see how functions become descriptors
- Create simple and practical metaclasses to enforce invariants or register classes
- Know when to use decorators vs metaclasses

### Theory (as in Python docs)

- Descriptors protocol
  - __get__, __set__, __delete__; data vs non-data descriptors; precedence with instance __dict__
- Function descriptors
  - Methods binding; functions as descriptors; bound/unbound methods background
- property / staticmethod / classmethod
  - How they work under the hood; common idioms
- Metaclasses
  - type as the metaclass of new-style classes; __new__ vs __init__ in metaclasses
  - __prepare__ hook, class namespace building; controlling attribute injection
  - Valid use-cases: validation, registration, singletons (with caveats), ABCs (mention)
- Hooks
  - __getattr__/__getattribute__, __setattr__, class creation hooks

### Practical examples (scripts in 13_metaprogramming)

- 01-descriptors.py — custom descriptor implementation
- 02-property.py — properties for attribute control
- 03-staticmethod.py — static/class methods examples
- 04-call.py — callable objects and __call__
- 05-meta.py — minimal metaclass controlling class creation
- 06-strict.py — metaclass enforcing strict attributes or validation
- 07-hooks.py — attribute access/creation hooks

## Chapter 14. Modules and Packages

This chapter explains Python's import system, package structure, module objects, and practical patterns for organizing code and dependencies.

### Goals

- Understand how imports work and how Python locates modules
- Organize code into packages; use relative and absolute imports correctly
- Control module exports and side effects
- Dynamically load modules when needed

### Theory (as in Python docs)

- Modules as singletons; module attributes (__name__, __file__, __package__, __all__)
- Import mechanics
  - sys.path search; packages and namespaces; __init__.py roles
  - Absolute vs relative imports; when to prefer each
  - Import time side-effects; idempotent imports
- Controlling exports
  - __all__, re-exporting, and public API design
- Dynamic imports
  - importlib.import_module; conditional imports for optional deps

### Practical examples (scripts in 14_modules)

- 01-imports.py — module attributes and import behaviors
- 02-packages.py — working with packages and relative imports
- small_module.py — a simple module used by examples
- small_package/ — a tiny package demonstrating package layout

## Chapter 15. Testing

This chapter introduces testing foundations and practical tools in Python, focusing on unit tests, fixtures, and property-based thinking.

### Goals

- Write basic tests and assertions; structure testable code
- Use unittest for test cases, fixtures, and assertions
- Understand test isolation, setup/teardown, and dependency injection basics
- Explore property-based tests and invariants

### Theory (as in Python docs)

- Why test? The pyramid concept; fast feedback
- unittest framework
  - TestCase, subTest, setUp/tearDown, setUpClass/tearDownClass
  - Skipping, expected failures
- Assertions
  - assertEqual, assertTrue/False, assertRaises, custom messages
- Fixtures and isolation
  - Temporary files/dirs, environment variables; mocking note
- Property-based approach
  - Deterministic invariants; shrinking idea (intro)

### Practical examples (scripts in 15_testing)

- 01-testing.py — ad-hoc tests and simple assertions
- 02-unittest.py — a minimal unittest suite
- 03-fixture.py — test fixtures and isolation patterns
- 04-property.py — property-like tests without external libs

