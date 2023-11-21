import sys
import io

__doc__ = """File API in Python
Available modes:
r - read
w - write
a - append
x - exclusive creation
t - text
b - binary
+ - read and write

Before Python 3.7 default encoding was the same as system encoding
After 3.7 it is UTF-8
You can define PYTHONUTF8 environment variable to change it
"""


def file_read():
    """
    Read file
    """
    with open('04-files.py', 'r') as file:
        print(file.read())


def file_readline():
    """
    Read file line by line
    Delimiting character is \n and can't be changed
    """
    with open('04-files.py', 'r') as file:
        for line in file:
            print(line, end='')


def write_file():
    """
    Write to file
    """
    with open('example.txt', 'w') as file:
        file.write('Hello World')


def write_append():
    """
    Append to file
    """
    with open('example.txt', 'a') as file:
        file.write('\nHello World2')


def show_seek():
    """
    Show seek()
    Used to change the file pointer's position within the file.
    Offset specifies the number of bytes to move the pointer
    Positive offset moves the pointer forward, negative offset moves it backward
    whence determines the reference point for the offset:
    0 (default): Offset is relative to the beginning of the file.
    1: Offset is relative to the current file position.
    2: Offset is relative to the end of the file.
    """
    with open('04-files.py', 'r') as file:
        print(file.read(10))
        file.seek(0)
        print(file.read(10))
        file.seek(5, 0)
        print(file.read(10))


def show_buffer():
    """
    Buffered file io
    Optimization to reduce the number of system calls
    """
    with open('04-files.py', 'r', buffering=1) as file:
        print(file.read(10))
        file.seek(0)
        print(file.read(10))
        file.seek(5, 0)
        print(file.read(10))


def show_tell():
    """
    Show tell()
    Returns the current position of the file pointer in bytes from the beginning of the file.
    It can be used to keep track of the file position or to later return to the current position
    """
    with open('04-files.py', 'r') as file:
        print(file.read(10))
        print(f"Current position: {file.tell()}")
        file.seek(0)
        print(file.read(10))
        print(f"Current position: {file.tell()}")
        file.seek(5, 0)
        print(file.read(10))
        print(f"Current position: {file.tell()}")


def in_memory_file():
    """
    In memory file behaves like a regular file
    Often used when you want to perform I/O operations on strings
    without actually reading from or writing to physical file (e.g. unit tests)
    """
    # StringIO
    file = io.StringIO()
    file.write('Hello World')
    print(file.getvalue())

    # BytesIO
    file = io.BytesIO()
    file.write(b'Hello World')
    print(file.getvalue())


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
