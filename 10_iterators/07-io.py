__doc__ = """Generators and IO operations

The ExitStack allows you to manage multiple context managers within a single context, 
and it ensures that all of these managers are properly exited and cleaned up when the context is exited.
Use Cases: ExitStack is commonly used when you have a variable number of context managers that need to be handled, 
especially in situations where you need to ensure that all context managers are exited correctly.

It can be represented as a number of a number of nested 'with' statements
"""

from contextlib import ExitStack
from heapq import merge


def merge_sorted_files(input_files, result):
    """
    Merge sorted files into one sorted file
    If any file read end up with an exception, the context manager will close all files correctly
    Files can be of any size, they are not loaded into memory at once
    In Java this can be done with Streams API
    :param input_files: files with sorted lines
    :param result:
    """
    with open(result, 'w') as result_file, ExitStack() as stack:
        files = [stack.enter_context(open(file)) for file in input_files]
        for sorted_line in merge(*files):
            result_file.write(sorted_line)


merge_sorted_files(['file1.txt', 'file2.txt'], 'result.txt')
with open('result.txt') as f:
    for line in f:
        print(line, end='')
