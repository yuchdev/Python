import importlib

from small_package.package_file import SelfReflection, self_reflection

__doc__ = """Package in Python is a way to organize modules
* Module is defined by __init__.py file in the directory
* File __init__.py can be empty or almost empty
* Submodules by default are not imported when you import a package
* Module is mutable object, so you can add new attributes to it
* Relative imports are imports from the current package and don't depend on sys.path
    * `from . import module` means import module from current package
    * `from .. import module` means import module from parent package
* `__package__` is the name of the package of the module
* For packageless scripts `__package__` is `None`

Pattern Facade
* Facade is a design pattern that provides a simplified interface to a larger body of code
* Package user and package developer use different APIs 
* User API is small, developer API is large
* User API is broken to multiple submodules
* We can define `__all__` variable in every submodule to define what is exported to user API
  and concatenate them in __init__.py
  
Creating Virtual Environment
* Virtual environment is a directory that contains all the necessary executables to use the packages
* Classic way to create virtual environment is to use `venv` module
* New tool is `pipenv` that combines `pip` and `virtualenv` in one tool
* `pipenv` creates virtual environment in `~/.local/share/virtualenvs` by default
* It is different than requirements.txt, because it also contains information about virtual environment 
  and transitive dependencies
"""

# Package user API
mc = SelfReflection()
mc.print()
self_reflection()


# Lazy imports
class LazyImporter:
    """
    LazyImporter is a class that can be used to import modules on demand
    """
    def __getattr__(self, name):
        """
        Method is called when an attribute is accessed, and uses importlib.import_module
        only when the attribute is first accessed
        :param name: name of the attribute 
        :return: attribute
        """
        module = importlib.import_module("small_package.package_file")
        return getattr(module, name)


# Usage
lazy_imports = LazyImporter()

# Lazy access the objects
lazy_imports.self_reflection()
obj = lazy_imports.SelfReflection()
