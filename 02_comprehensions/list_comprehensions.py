import os
import sys
import glob


def create():

    # A list comprehension provides a compact way of mapping a list into another list by applying a function
    a_list = [1, 2, 3, 4]
    print("a_list={}".format(a_list))
    a_list2 = [elem * 2 for elem in a_list]
    print("[elem*2 for elem in a_list]={0}".format(a_list2))

    # another example
    names = ['Elwood', 'Jake']
    print("names={}".format(names))
    names2 = [name.lower() for name in names]
    print("[name.lower() for name in names]={}".format(names2))


def files():
    # it does not change the original list
    files_in_dir = [os.path.realpath(f) for f in glob.glob('*.py')]
    print("[os.path.realpath(f) for f in glob.glob('*.py')]={}".format(files_in_dir))

    # List comprehensions can also filter items
    big_in_dir = [os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600]
    print("[os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600]={}".format(big_in_dir))

    # there’s no limit to how complex a list comprehension can be
    sizes = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
    print("[(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]={}".format(sizes))


def queries():
    stocks = [
        {'price': 91.10, 'name': 'IBM', 'shares': 50},
        {'price': 83.44, 'name': 'CAT', 'shares': 150},
        {'price': 51.23, 'name': 'MSFT', 'shares': 200},
        {'price': 40.37, 'name': 'GE', 'shares': 95},
        {'price': 65.10, 'name': 'MSFT', 'shares': 50},
        {'price': 70.44, 'name': 'IBM', 'shares': 100}
    ]
    print("stocks={}".format(stocks))

    stocknames = [s['name'] for s in stocks]
    print("[s['name'] for s in stocks]={}".format(stocknames))

    # You can perform database-like queries on sequences
    query = [s for s in stocks if s['price'] > 50.0 and s['shares'] > 100]
    print("[s for s in stocks if s['price'] > 50.0 and s['shares'] > 100]={}".format(query))

    query = [s for s in stocks if s['name'] in ('MSFT', 'IBM')]
    print("[s for s in stocks if s['name'] in ('MSFT', 'IBM')]={}".format(query))

    # combine a list comprehension with a sequence reduction
    cost = sum([s['shares'] * s['price'] for s in stocks])
    print("sum([s['shares'] * s['price'] for s in stocks])={}".format(cost))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call: create, files, queries")
