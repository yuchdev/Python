__doc__ = """Package in Python is a way to organize modules.
It is defined by __init__.py file in the directory.
__package__ is the name of the package of the module.
"""


def self_reflection():
    print("Package name: {}".format(__name__))
    print("Package file: {}".format(__file__))
    print("Package doc: {}".format(__doc__))
    print("Package package: {}".format(__package__))


class SelfReflection:
    def __init__(self):
        print("Module class")

    def print(self):
        print("ModuleClass.print")
