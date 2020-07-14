import os
import stat
import glob


def show_list_comprehensions():
    # A list comprehension provides a compact way of mapping a list into another list by applying a function
    a_list = [1, 2, 3, 4]
    print([elem*2 for elem in a_list])

    # it does not change the original list

    files_in_dir = [os.path.realpath(f) for f in glob.glob('*.py')]
    print(files_in_dir)

    # List comprehensions can also filter items
    big_in_dir = [os.path.realpath(f) for f in glob.glob('*.py') if os.stat(f).st_size > 600]
    print(big_in_dir)

    # there’s no limit to how complex a list comprehension can be
    sizes = [(os.stat(f).st_size, os.path.realpath(f)) for f in glob.glob('*.py')]
    print(sizes)

