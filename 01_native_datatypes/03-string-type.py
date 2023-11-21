__doc__ = """In Python, the string type (str) is used to represent textual data. 
Strings in Python are immutable, meaning their values cannot be changed after they are created. 
Here's a detailed overview of the Python string type
"""

# Strings can be created using single quotes ('), double quotes ("), or triple quotes (''' or """) for multiline strings
single_quoted_str = 'Hello, World!'
double_quoted_str = "Hello, World!"
multiline_str = '''This is a
multiline string.'''


# Strings can be concatenated using the + operator
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"


# Strings can be indexed and sliced.
# Indexing starts at 0, and negative indices represent positions from the end of the string
my_string = "Python"
first_char = my_string[0]     # 'P'
last_char = my_string[-1]     # 'n'
substring = my_string[1:4]    # 'yth'

# Strings have a variety of built-in methods for common operations such as case conversion, 
# finding substrings, replacing text, and more
my_string = "Hello, World!"
upper_case = my_string.upper()
lower_case = my_string.lower()
contains_world = my_string.find("World")
replaced_str = my_string.replace("Hello", "Hi")

# Python provides multiple ways to format strings, 
# including the % operator, the format() method, and f-strings (formatted string literals)
# Examples
name = "Alice"
age = 30
formatted_str = "Name: %s, Age: %d" % (name, age)
formatted_str2 = "Name: {}, Age: {}".format(name, age)
f_string = f"Name: {name}, Age: {age}"

# Special characters in strings can be represented using escape characters, 
# such as \n for a newline or \t for a tab
escaped_str = "This is a line\nThis is a new line"

# Raw strings can be created by prefixing a string literal with r
# This is useful when dealing with regular expressions or file paths where backslashes need to be preserved
raw_str = r"C:\Users\Alice\Documents"

# Python supports various operations on strings, including checking for substring existence, 
# string length, and repetition
is_substring = "Hello" in "Hello, World!"
str_length = len("Python")
repeated_str = "abc" * 3  # 'abcabcabc'

# Strings in Python are immutable, meaning their values cannot be changed after creation
# However, new strings can be created through operations like concatenation and slicing
original_str = "Python"
new_str = original_str + " 3"
