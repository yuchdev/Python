import sys
import small_module

__doc__ = """Import in Python is a way to include other modules.
* Like anything else in Python, a module is also an object, and import is executable statement.
* Modules lookup
    * Look in sys.modules
    * Current directory
    * Modules in sys.path
    * Site-packages
    * PYTHONPATH
* Module is imported only once
* Import is transitive, so if we import * from a module, we also import all the modules that it imports
* It can be overwritten by using `__all__` variable
* You can call `import something` from any place in the code, but it's not recommended by PEP8
* `import *` can't be written inside a function because it's not known at "compile time"
* Don't try to save lines by importing multiple modules in one line, e.g. `import os, sys`
* You can group imports in following way:
    * Standard library imports
    * Third-party imports
    * Local application imports
* Import performed once, as a singleton operation
* Import calls `__import__()` internal function
* Library importlib contains tools like `import_module()` and `reload()`
* Cyclic imports generally don't break the program immediately, but should be avoided
* You can use importlib for things like "lazy" imports, customization of sys.meta_path, etc.
* `sys.path_hooks` is a list of callables that importlib uses to find modules
* `sys.meta_path` is a list of importers that are called on every import
* Import ecosystem has been developed non-linear over time, that's why it may seem inconsistent
"""


def enumerate_module():
    """
    Even empty module contains attributes
    """
    print("small_module attributes", dir(small_module))


def show_builtins():
    """
    Most modules have the name __builtins__ made available as part of their globals
    it contains globals like dir(), open(), None etc
    """
    print("__builtins__", small_module.__builtins__)


def print_module():
    """
    Print all information about module
    """
    print("Module name: {}".format(small_module.__name__))
    print("Module file: {}".format(small_module.__file__))
    print("Module doc: {}".format(small_module.__doc__))
    print("Module package: {}".format(small_module.__package__))
    print("Module loader: {}".format(small_module.__loader__))
    print("Module cached: {}".format(small_module.__cached__))
    print("Module spec: {}".format(small_module.__spec__))
    print("Module builtins: {}".format(small_module.__builtins__))
    print("Module globals: {}".format(small_module.__dict__))
    print("Module attributes: {}".format(dir(small_module)))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
