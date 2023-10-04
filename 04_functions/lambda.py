import sys

__doc__ = """Lambda is a function without a name
Common syntax:
    lambda argument_list: expression
Lambda uses: 
    - sort key
    - filter
    - map/reduce
    - decorators
    - closures
    - currying
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
