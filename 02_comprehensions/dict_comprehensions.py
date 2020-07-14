import os
import stat
import glob


def show_dict_comprehensions():
    # A dictionary comprehension is like a list comprehension, but it constructs a dictionary instead of a list
    metadata_dict = {f: os.stat(f) for f in glob.glob('*.py')}
    print(metadata_dict)

    # Here’s a trick with dictionary comprehensions that might be useful someday:
    # swapping the keys and values of a dictionary (value also must be hashable)
    a_dict = {'a': 1, 'b': 2, 'c': 3}
    rev_dict = {value: key for key, value in a_dict.items()}
    print(a_dict)
    print(rev_dict)

