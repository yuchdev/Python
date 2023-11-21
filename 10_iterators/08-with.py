import os
from contextlib import contextmanager

__doc__ = """Generators can be used with context managers
Context managers allow you to allocate and release resources precisely when you want to.
The most widely used example of context managers is the 'with' statement.
Examples are below
"""


# Implement 'cd' generator
@contextmanager
def cd(path):
    """
    Change directory
    :param path:
    :return:
    """
    old_path = os.getcwd()
    os.chdir(path)
    try:
        # yield is used to return a generator
        yield
    finally:
        os.chdir(old_path)


# Example of usage
with cd('..'):
    print(f"Current directory: {os.getcwd()}")

print(f"Current directory: {os.getcwd()}")


# Implement 'tempfile' generator
@contextmanager
def tempfile(name):
    """
    Create a temporary file
    :param name:
    :return:
    """
    temp_f = None
    try:
        temp_f = open(name, 'w')
        yield temp_f
    finally:
        temp_f.close()
        os.remove(name)


# Example of usage
with tempfile('temp.txt') as f:
    f.write('Hello, world!')
    f.write('Bye, world!')
