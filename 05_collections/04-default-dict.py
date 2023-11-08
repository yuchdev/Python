import sys
from collections import defaultdict

__doc__ = """Default dict is a subclass of dict that returns a default value when a key is not present.
"""


def show_defaultdict():
    """
    Create default dict
    """
    dd = defaultdict(list)
    dd['dogs'].append('Rufus')
    dd['dogs'].append('Kathrin')
    dd['dogs'].append('Mr Sniffles')
    dd['cats'].append('Fluffy')
    print(dd)
    print(dd['dogs'])
    print(dd['cats'])
    print(dd['monkeys'])


def show_lambda():
    """
    For default, we can pass function that will be called when key is not present
    """
    class Counter:
        def __init__(self):
            self.counter = 0

        def __call__(self):
            self.counter += 1
            return self.counter

    dd = defaultdict(lambda: Counter)
    print(dd['dogs']())
    print(dd['dogs']())
    print(dd['cats']())
    print(dd['cats']())


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
