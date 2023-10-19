# Python course

## Chapter 1. Native datatypes

### Module usage

* import path
* default attributes of empty module (__name__, __module__ etc)

### Numeric

* boolean, integer, float, and complex
* numeric operations +, -, *, **, /, //
* math.py, sys.maxint

### String

* bytes string: encode/decode()
* unicode string
* r"" and f"" forms

### List

* mutable, single types elements
* represented as list of pointers
* indexing and slicing

### Tuple

* immutable, different types elements
* could be dict key
* (a,b,c) = x

### Set and Dict

* Represented as hash table
* keys() return set
* values() and items() return list

### Files

* open and "with" statement
* read() - read all content
* "in", readlines() - read all lines

## Chapter 2. Comprehensions

### List

* list comprehension provides a compact way of mapping a list into another list
* filesystem comprehension example
* map() and filter() functions
* combine a list comprehension with a sequence reduction
* we can perform database-like queries on sequences
* walrus operator allows you to run an expression while simultaneously assigning the output value
* matrix comprehension example
* list comprehension in Python works by loading the entire output list into memory
* it’s often helpful to use a generator instead of a list comprehension in Python

### Dict

* dictionary comprehension similar to list comprehension, but it operates with key-value pairs
* swapping the keys and values of a dictionary example (value also must be hashable and unique)

## Chapter 3. Functions

### Function as object

* function objects has a number of attributes:
    * __doc__ is the function’s documentation string
    * __name__ is the function’s name
    * __defaults__ is a tuple containing default argument values for those arguments that have defaults, or None if no
      arguments have a default value
    * __code__ is the code object representing the compiled function body
    * __globals__ is a reference to the dictionary that holds the function’s global variables — the global namespace of
      the module in which the function was defined
    * __dict__ is the namespace supporting arbitrary function attributes
    * __closure__ is None or a tuple of cells that contain bindings for the function’s free variables
    * __annotations__ is a dictionary containing annotations of parameters
    * __kwdefaults__ is a dictionary containing defaults for keyword-only parameters
    * __call__ is a method that allows the function to be called
    * __get__ is a method that returns a bound method object when the function is an instance attribute
* id() function returns an integer representing its identity
* Bytecode of function can be obtained by dis module

### Function arguments

* arguments is a tuple
* arguments can be passed by position or by keyword
* arguments can be empty
* you can Guarantee at least one argument by using *args
* arguments can have default values
* default values are evaluated at the point of function definition. That's why you can't use mutable objects (e.g. set)
  as default values
* use None as default value and check it inside function
* arguments can be packed (while func definition) and unpacked (while calling)
* unpacking arguments as a list or dictionary
* flatten() example
* keyargs() example

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
