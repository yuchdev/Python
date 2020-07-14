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


def append():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)

    # Assigning a value to an existing key will wipe out the old value
    # Dictionary values can be any datatype, including integers, booleans, or even other dictionaries
    # And within a single dictionary, the values don’t all need to be the same type
    # Dictionary keys are more restricted, but they can be strings, integers, and a few other types
    a_dict['user'] = 'mark'
    print("a_dict['user'] = 'mark': ", a_dict)


def search():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)
    print("len(a_dict) =", len(a_dict))
    print("'user' in a_dict:] =", 'user' in a_dict)

    # accessor with default value
    print("a_dict.get('user', 'atatat') =", a_dict.get('user', 'atatat'))

    # None is a special constant in Python. It is a null value
    a_dict['None'] = None
    print("a_dict['None'] = None:", a_dict)


def operations():
    a_dict = {'server': 'db.atatat.org', 'database': 'mysql'}
    print("a_dict =", a_dict)

    a_keys: list = a_dict.keys()
    print("a_dict.keys() =", a_keys)

    vals: list = a_dict.values()
    print("a_dict.values() =", vals)

    item_pairs: list = a_dict.items()
    print("a_dict.items() =", item_pairs)
    print("for k, v in item_pairs:")
    for k, v in item_pairs:
        print(k, v)


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create, append, search")
