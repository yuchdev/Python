import sys

__doc__ = """Show examples of debug print decorators.
From naive to production implementation.
"""

if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
