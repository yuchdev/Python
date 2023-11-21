import re

# TODO: This chapter is a stub. Organize this module.

__doc__ = """The re module provides several functions, but the most commonly used ones are:
re.search(pattern, string): Searches for a match anywhere in the string.
re.match(pattern, string): Matches only at the beginning of the string.
re.findall(pattern, string): Finds all occurrences of the pattern in the string.
re.sub(pattern, replacement, string): Replaces occurrences of the pattern with the specified replacement.
"""

# Example 1: Search for a pattern
pattern = re.compile(r'\d+')
result = pattern.search('Age: 25, Height: 180 cm')
print(result.group())  # Output: 25

# Example 2: Find all occurrences
pattern = re.compile(r'\b\w{3}\b')
result = pattern.findall('The cat is on the mat')
print(result)  # Output: ['The', 'cat', 'on', 'the', 'mat']

# Example 3: Replace pattern in a string
pattern = re.compile(r'\s+')
result = pattern.sub('-', 'Hello   World')
print(result)  # Output: Hello-World


# Greedy vs. Non-Greedy Matching
# By default, quantifiers are greedy, meaning they match as much text as possible
# Adding a ? makes them non-greedy
pattern = re.compile(r'<.*?>')
result = pattern.search('<div>Hello</div>')
print(result.group())  # Output: <div>

# Lookahead and Lookbehind
# You can use lookahead ((?=...)) and lookbehind ((?<=...)) assertions 
# to check for patterns ahead or behind the current position without including them in the match
pattern = re.compile(r'(?<=@)\w+')
result = pattern.search('user@example.com')
print(result.group())  # Output: example


# Performance Considerations
# Compile Regular Expressions
# If you're using a regular expression frequently, consider compiling it with re.compile()
# This can improve performance, especially in a loop
pattern = re.compile(r'\d+')
for text in text_list:
    result = pattern.search(text)

# Use Specificity
# Try to make your regular expressions as specific as possible. Broad patterns may lead to inefficient matching

# Avoid Backtracking
# Be cautious with patterns that involve backtracking, as it can lead to poor performance on large strings

# Profiling
# If you have concerns about performance, use Python's timeit module or other profiling tools 
# to identify bottlenecks in your regular expressions

