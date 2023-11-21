from traceback import print_tb, format_exc

__doc__ = """Python offers following exception API:
* you can pass any number of arguments to Exception constructor
* you can access exception arguments via Exception.args attribute.
  You can use it for passing additional information to the handler
* you can access exception traceback via Exception.__traceback__ attribute
  This allows passing entire exception context to the handler
* you can access exception type via Exception.__class__ attribute
  This is how you can check exception type in except block
* Traceback is being created only if exception is being raised
  It is None on Exception.__init__ call, and initialized on raise
* It's the advantage of dynamic languages like Python. E.g. in Java or C++ 
  stacktrace is being created on Exception constructor call
  It makes exception creation in Python much faster
* Traceback filled with information dynamically in the moment of passing stack layers
* Methods __str__() and __repr__() are being called on exception printing
  They are usually not very informative
* In order to get more information about exception you can use traceback module
* You can use traceback.format_exc() to print exception
* You can use traceback.print_tb() to print exception traceback to stdout
"""


# you can pass any number of arguments to Exception constructor
try:
    raise RuntimeError(1, 2, 3)
except RuntimeError as e:
    print(f"e.args: {e.args}")
    print(f"Formatted exception: {format_exc()}")


# you can access exception traceback via Exception.__traceback__ attribute
def lower_level():
    raise RuntimeError("lower_level exception")


def middle_level():
    lower_level()


def upper_level():
    middle_level()


try:
    upper_level()
except RuntimeError as e:
    print("Exception traceback from upper_level()")
    print(f"e.__traceback__: {e.__traceback__}")
    print(f"e.__traceback__.print_tb(): {print_tb(e.__traceback__)}")
    print(f"e.__traceback__.tb_frame: {e.__traceback__.tb_frame}")
    print(f"e.__traceback__.tb_lineno: {e.__traceback__.tb_lineno}")
    print(f"e.__traceback__.tb_next: {e.__traceback__.tb_next}")
