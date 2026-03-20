# Chapter 3. Functions

This chapter explores functions in Python as first-class objects, their argument passing mechanisms, scope rules, and lambda functions.

## Function as an Object
In Python, functions are first-class objects, meaning they can be assigned to variables, passed as arguments, and returned from other functions.
* **Introspection**: Use `dir(func)` to see all attributes and `id(func)` for its unique identity.
* **Bytecode**: The `dis` module can be used to inspect the compiled bytecode of a function: `dis.dis(func)`.
* **Attributes**:
    * `__doc__`: The function’s documentation string.
    * `__name__`: The function’s name.
    * `__defaults__`: Tuple of default values for positional/keyword-or-positional arguments.
    * `__kwdefaults__`: Dictionary of default values for keyword-only arguments.
    * `__code__`: The compiled function body (bytecode).
    * `__globals__`: Reference to the module's global namespace.
    * `__annotations__`: Dictionary containing parameter and return annotations.

## Function Arguments
Python offers flexible ways to pass arguments:
* **Positional & Keyword**: Arguments can be passed by position or by name.
* **Variadic Arguments (`*args`)**: Collects extra positional arguments into a tuple. Use `def func(first, *args)` to require at least one argument.
* **Keyword-Only Arguments (`*`, ...)**: Arguments defined after a bare `*` or `*args` must be passed as keyword arguments.
* **Arbitrary Keyword Arguments (`**kwargs`)**: Collects extra keyword arguments into a dictionary.
* **Unpacking**: Use `*` to unpack a list/tuple and `**` to unpack a dictionary into function arguments.
* **Mutable Defaults Pitfall**: Default values are evaluated at **definition time**. Avoid using mutable objects (like `[]` or `{}`) as defaults; use `None` and initialize inside the function instead.

## Function Scope
Python follows the **LEGB** rule for name resolution:
1. **Local**: Defined inside the current function.
2. **Enclosing**: Defined in nested function structures (closures).
3. **Global**: Defined at the top level of the module.
4. **Built-in**: Preassigned names in Python (e.g., `len`, `min`).

### Keywords:
* `global`: Allows modifying a variable at the module level.
* `nonlocal`: Allows modifying a variable in the nearest enclosing scope (excluding globals).
* `globals()` / `locals()`: Returns dictionaries of the current global and local symbol tables.

## Lambda Functions
Lambdas are small, anonymous, single-expression functions.
* **Syntax**: `lambda arguments: expression`
* **Use Cases**: Quick transformations, sorting keys, and functional programming patterns (map, filter).

---
### Examples
* `01-function-object.py`: Introspection, attributes, and bytecode.
* `02-arguments.py`: `*args`, `**kwargs`, unpacking, and the mutable default value trick.
* `03-scope.py`: LEGB rules, `global`, `nonlocal`, and closures.
* `04-lambda.py`: Lambda syntax and common applications.
