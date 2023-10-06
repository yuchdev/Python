import sys

__doc__ = """
"""


def show_string():
    """
    Information about string
    """
    # Quotes don't make difference
    print("Hello World")
    print('Hello World')
    print("""Hello World""")

    # Raw string
    print(r"Hello\nWorld")

    # You can access individual characters
    # Character itself is a string
    print(type("Hello"[1]))

    # You can find the length of a string using the len() function
    # It can differ from number of characters
    print("Length of Hello\nWorld:")
    print(len("Hello\nWorld"))

    # Strings are immutable
    # You can't change a character in a string (or delete it)
    # You can only create a new string
    low_string = "hello world"
    new_string = low_string.capitalize()
    print(low_string)
    print(new_string)


def show_properties():
    """
    Show properties of string
    """
    print("isascii(): ")
    print("hello world".isascii())
    print("islower(): ")
    print("hello world".islower())
    print("isupper(): ")
    print("hello world".isupper())
    print("istitle(): ")
    print("hello world".istitle())
    print("isalpha(): ")
    print("hello world".isalpha())
    print("isalnum(): ")
    print("hello world".isalnum())
    print("isdecimal(): ")
    print("hello world".isdecimal())
    print("isspace(): ")
    print("hello world".isspace())


def show_format():
    """
    There are 3 ways to format strings in Python
    """
    # 1. Using % operator
    print("Hello %s" % "World")

    # 2. Using format() method
    print("Hello {}".format("World"))

    # 3. Using f-strings (Python 3.6+, preferred way)
    print(f"Hello {'World'}")


def show_alignment():
    """
    Show alignment
    """
    # Left alignment
    print(f"{'Hello':<10}{'World'}")

    # Right alignment
    print(f"{'Hello':>10}{'World'}")

    # Center alignment
    print(f"{'Hello':^10}{'World'}")


def show_padding():
    """
    Show padding
    """
    # Padding with zeros
    print(f"{'Hello':0>10}{'World'}")

    # Padding with any character
    print(f"{'Hello':#>10}{'World'}")


def show_truncation():
    """
    Show truncation
    """
    # Truncate to 3 characters
    print(f"{'Hello':.3}{'World'}")

    # Truncate to 3 characters and pad with zeros
    print(f"{'Hello':0>10.3}{'World'}")


def show_format_numbers():
    """
    Show format specification for numbers
    """
    # Format specification
    print(f"{3.1415926535:.3f}")

    # Format specification for integers
    print(f"{1000000000:,}")

    # Format specification for binary
    print(f"{255:b}")

    # Format specification for hexadecimal
    print(f"{255:x}")

    # Format specification for octal
    print(f"{255:o}")

    # Format specification for scientific notation
    print(f"{3.1415926535:e}")

    # Format specification for percentage
    print(f"{0.25:%}")

    # Format specification for currency
    print(f"{1000000.25:$>10,.2f}")


def show_split():
    """
    Show split method
    """
    # Split a string into a list of substrings separated by a delimiter
    print("Hello World".split(" "))

    # Split a string into a list of substrings separated by a delimiter
    # and limit the number of splits
    print("Hello World".split(" ", 1))

    # Split a string into a list of substrings separated by any symbol
    print("Hello_World".split("_"))


def show_search():
    """
    Ways to look for a substring in a string
    """
    # Find the index of the first occurrence of a substring in a string
    print("Hello World".find("World"))

    # Find the index of the first occurrence of a substring in a string
    # If not found, return -1
    print("Hello World".find("World!"))

    # Find the index of the first occurrence of a substring in a string
    # If not found, raise an exception
    print("Hello World".index("World!"))


def show_format_sql():
    """
    Not every time Python formatting fits the best
    E.g. formatting SQL queries may cause problems
    Replacing {} could be used for SQL injection
    """
    # Incorrect way:
    print(f"SELECT * FROM table WHERE id = {1}")

    # Correct way:
    limit = 10
    offset = 0
    batch_query = f"SELECT * FROM table LIMIT %s OFFSET %s"
    sql_query = (batch_query, (limit, offset))
    print(sql_query)


def show_str_repr():
    """
    Show difference between str() and repr()
    str() is used to create a human-readable or "informal" string representation of an object
    repr() is used to create an unambiguous or "formal" string representation of an object
    You can define __str__() and __repr__() methods in your class
    """
    number = 42
    str_representation = str(number)
    print(str_representation)  # Output: '42'
    repr_representation = repr(number)
    print(repr_representation)  # Output: '42'


def show_bytes():
    """
    String abd bytes are different, but have similar APIs
    """
    # String
    print("Hello World")
    print(b"Hello World")

    # String to bytes, bytes to string
    print("Hello World".encode('utf-8'))
    print(b"Hello World".decode('utf-8'))

    # Bytes API
    print(b"Hello World".startswith(b"Hello"))
    print(b"Hello World".endswith(b"World"))
    print(b"Hello World".split(b" "))
    print(b"Hello World".find(b"World"))



if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
