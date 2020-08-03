import sys


def create():
    """
    Dictionary operations
    """
    print('Dictionary create')

    # A dictionary is an unordered set of key-value pairs (based on hash)
    # The syntax is similar to sets, but instead of values, you have key-value pairs
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}

    # You can get values by key, but you can’t get keys by value
    print("a_dict =", a_dict)
    print("a_dict['server'] =", a_dict['server'])
    print("a_dict['database'] =", a_dict['database'])

    # Alternative way:
    # The zip function takes multiple sequences and makes an iterator that combines them
    keys: list = ['server', 'database', 'user']
    values: list = ['atatat.com', 'oracle', 'mitch']
    pairs = zip(keys, values)
    # zip object is not dict or list yet, though
    print("zip(keys, values) = {}".format(pairs))
    dict_pairs = dict(pairs)
    print("dict(pairs) = {}".format(dict_pairs))

    # Sequences should be equal length
    # zip() stops once the shortest input sequence is exhausted
    values.pop()
    print("values.pop(); dict(zip(keys, values))", dict(zip(keys, values)))


def append():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)

    # Assigning a value to an existing key will wipe out the old value
    # Dictionary values can be any datatype, including integers, booleans, or even other dictionaries
    # And within a single dictionary, the values don’t all need to be the same type
    # Dictionary keys are more restricted, but they can be strings, integers, and a few other types
    a_dict[1] = 'mark'
    print("a_dict['user'] = 'mark': ", a_dict)

    # Neither a list, a set, nor another dictionary can serve as a dictionary key,
    # because lists and dictionaries are mutable


def remove():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    # To delete a value use the del statement
    del a_dict['server']


def search():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)
    print("len(a_dict) =", len(a_dict))
    print("'user' in a_dict =", 'user' in a_dict)

    # accessor with default value
    print("a_dict.get('user', 'atatat') =", a_dict.get('user', 'atatat'))

    # None is a special constant in Python. It is a null value
    a_dict['None'] = None
    print("a_dict['None'] = None:", a_dict)


def operations():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)

    a_keys = a_dict.keys()
    print("a_dict.keys() =", a_keys)

    # If you turn a dictionary into a list, you also get all of its keys
    print("list(a_dict) =", list(a_dict))

    vals = a_dict.values()
    print("a_dict.values() =", vals)

    item_pairs = a_dict.items()
    print("a_dict.items() =", item_pairs)
    print("for k, v in item_pairs:")
    for k, v in item_pairs:
        print(k, v)

    # You can invert a dictionary using zip()
    inverted_dict = dict(zip(vals, a_keys))
    print("dict(zip(vals, a_keys)): {}".format(inverted_dict))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
