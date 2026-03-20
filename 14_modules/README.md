# Chapter 14. Modules & Packages

This chapter explains Python's import system, how modules are located and loaded, and how to organize code into packages.

## Modules
A module is a file containing Python definitions and statements.
* **Singleton Nature**: Modules are only executed once when first imported. Subsequent imports return the same module object from `sys.modules`.
* **Search Path**: Python looks for modules in `sys.modules`, then the current directory, then `PYTHONPATH`, and finally in the standard library and site-packages (`sys.path`).
* **Attributes**:
    * `__name__`: `"__main__"` if run directly, otherwise the module's name.
    * `__file__`: The path to the module file.
    * `__all__`: A list of strings defining what symbols are exported when `from module import *` is used.

## Packages
A package is a directory containing a special `__init__.py` file (and potentially other modules/subpackages).
* **`__init__.py`**: This file is executed when the package is imported. It's often used to export a simplified API from the package's internal modules.
* **Imports**:
    * **Absolute**: `import my_package.my_module`.
    * **Relative**: `from . import my_module` (only works within packages).

## Dynamic Imports
* **`importlib.import_module(name)`**: Programmatically import a module by its string name.
* **`importlib.reload(module)`**: Reloads a previously imported module (useful during development).

---
### Examples
* `01-imports.py`: Module attributes, the search path, and `sys.modules`.
* `02-packages.py`: Working with packages, `__init__.py`, and relative imports.
* `small_module.py`: A simple module used as a target for import examples.
* `small_package/`: A directory demonstrating a basic package structure.
