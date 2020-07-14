import empty_module


def enumerate_module():
    """
    Even empty module contains attributes
    """
    print("Empty_module attributes", dir(empty_module))


def show_builtins():
    """
    Most modules have the name __builtins__ made available as part of their globals
    it contains globals like dir(), open(), None etc
    """
    print("__builtins__", empty_module.__builtins__)


def show_others():
    """
    Other empty module default attributes
    """
    print("__cached__ is byte-compiled file name", empty_module.__cached__)
    print("__doc__ is docstring if present:", empty_module.__doc__)
    print("__file__ full file path, useful for os.path()", empty_module.__file__)
    print("__loader__ object used by internals when loading the module", empty_module.__loader__)
    print("Module __name__ if imported, __main__ is executed", empty_module.__name__)
    print("__package__ is package name if present", empty_module.__package__)
    print("__spec__ is module properties", empty_module.__spec__)


if __name__ == '__main__':
    show_others()

