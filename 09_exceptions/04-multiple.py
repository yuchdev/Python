__doc__ = """Multiple exceptions:
* In Python you can throw and handle multiple exceptions
* You can wrap one exception into another
* Exception.__context__ attribute contains exception that was raised before

4 forms of raise:
* raise exception without context 
    raise Exception
* old_exception is being saved in __context__
    raise Exception("message") from old_exception
* no cause 
    raise Exception("message") from None  
* re-raise exception with context
    raise 
    
* try can contain 'else' block
  It is used for code that should be executed only if no exception was raised
"""


def wrap_exception():
    """
    You can wrap one exception into another
    """
    try:
        raise KeyError("key")
    except KeyError as ex:
        old_exception = ex
        print(f"Old context: {ex.__context__}")
        print(f"Old cause: {ex.__cause__}")
        print(f"Old traceback: {ex.__traceback__}")
        print(f"Old type: {ex.__class__}")
        print(f"Old args: {ex.args}")
        # wrap old context
        raise ValueError("value") from old_exception


try:
    wrap_exception()
except ValueError as e:
    print(f"New context: {e.__context__}")
    print(f"New cause: {e.__cause__}")
    print(f"New traceback: {e.__traceback__}")
    print(f"New type: {e.__class__}")
    print(f"New args: {e.args}")


def multiple_exceptions():
    """
    You can throw multiple exceptions
    Each of them has its own context, traceback and cause
    """
    try:
        raise KeyError("key")
    except KeyError as ex:
        print(f"KeyError context: {ex.__context__}")
        print(f"KeyError cause: {ex.__cause__}")
        print(f"KeyError traceback: {ex.__traceback__}")
        print(f"KeyError type: {ex.__class__}")
        print(f"KeyError args: {ex.args}")
        raise ValueError("value")


try:
    multiple_exceptions()
except ValueError as e:
    print(f"ValueError context: {e.__context__}")
    print(f"ValueError cause: {e.__cause__}")
    print(f"ValueError traceback: {e.__traceback__}")
    print(f"ValueError type: {e.__class__}")
    print(f"ValueError args: {e.args}")


# Else block
try:
    print("No exception expected")
except RuntimeError:
    print("Should not be printed")
else:
    print("Report success")
