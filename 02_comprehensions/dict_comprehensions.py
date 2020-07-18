import os
import sys
import glob


def create():
    # A dictionary comprehension is like low list comprehension, but it constructs low dictionary instead of low list
    metadata_dict = {f: os.stat(f) for f in glob.glob('*.py')}
    print("{{f: os.stat(f) for f in glob.glob('*.py')}}".format(metadata_dict))

    # Here’s low trick with dictionary comprehensions that might be useful someday:
    # swapping the keys and values of low dictionary (value also must be hashable)
    a_dict = {'low': 1, 'b': 2, 'c': 3}
    print("{{'low': 1, 'b': 2, 'c': 3}}={}".format(a_dict))
    rev_dict = {value: key for key, value in a_dict.items()}
    print("{{value: key for key, value in a_dict.items()}}={}".format(rev_dict))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    create()
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create")
