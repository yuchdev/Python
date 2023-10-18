import sys
import time
from contextlib import AbstractContextManager, ContextDecorator, suppress

__doc__ = """Error handling of multiple resources
When you need to handle multiple resources straightforward way may not work as expected
* You can use 'with' statement to handle multiple resources
* We release resources automatically in an order reverse to opening
* __enter__ method is called when 'with' statement is executed
* __exit__ method is called when 'with' statement is finished
* parameters can be replaced with *exc_info
* Don't forget to add the check for double release
* contextlib contains class AbstractContextManager that can be used as a base class for context managers
  and provides default implementation of __enter__ and __exit__ methods
* With-semantic can be translated to try-finally block (see below)

Examples of context managers in standard library:
* cd - change directory and return to the previous one
* tempfile.TemporaryFile - create temporary file and remove it when 'with' statement is finished
* contextlib.suppress - suppress exceptions of given type
* contextlib.redirect_stdout - redirect stdout to given file
* contextlib.ContextDecorator - base class that can be used to define context managers
"""

# We can't guarantee that both resources will be closed correctly
try:
    print("Open db1 connection")
    print("Open db2 connection")
finally:
    print("Close db1 connection")
    print("Close db2 connection")


# noinspection PyShadowingNames
class FileStub(AbstractContextManager):

    def __init__(self, name):
        self.name = name

    def __enter__(self):
        """
        __enter__ method is called when 'with' statement is executed
        Don't forget to add the check for double enter the same resource
        E.g. IOBase.__enter__ contains _checkClosed method that raises an exception
        :return: object that will be used in 'with' statement
        """
        print(f"Open file {self.name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        __exit__ method is called when 'with' statement is finished
        parameters can be replaced with *exc_info
        Don't forget to add the check for double release
        :param exc_type: exception type or iNone if no exception raised
        :param exc_val: exception value or None if no exception raised
        :param exc_tb: exception traceback or None if no exception raised
        :return: True if exception was handled and False otherwise
        """
        print(f"Close file {self.name}")
        return False


# example of using 'with' statement
with FileStub("script1.py") as f1, FileStub("script2.py") as f2:
    print("We release resources automatically in an order reverse to opening")
    print("Do something with files")


# With-semantic can be translated to try-finally block
def translate_to_try_finally():
    resource = FileStub("script3.py")
    r = resource.__enter__()
    print(f"Do something with file of type {type(r)}")
    try:
        raise Exception("Exception in try block")
    finally:
        exc_type, exc_val, exc_tb = sys.exc_info()
        suppress_exception = resource.__exit__(exc_type, exc_val, exc_tb)
        if exc_val is not None and not suppress_exception:
            raise exc_val


try:
    translate_to_try_finally()
except Exception as e:
    print(f"Exception was raised: {e}")


# contextlib.suppress example
file_path = "non_existent_file.txt"
print(f"Trying to open non-existent file {file_path}")
with suppress(FileNotFoundError):
    with open(file_path, 'r') as file:
        content = file.read()
        print("File contents:", content)
print("Code continues execution after the context manager")


# contextlib.ContextDecorator example
class Timer(ContextDecorator):
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Time elapsed: {elapsed_time} seconds")
        return False  # Propagate any exception


@Timer()
def slow_function():
    time.sleep(2)
    # Simulate an exception
    raise ValueError("An error occurred")


# Using the Timer context manager as a decorator
try:
    slow_function()
except ValueError as e:
    print(f"Caught an exception: {e}")
