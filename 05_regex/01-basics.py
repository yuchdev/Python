import re

"""Quick tour of Python's re module (see README for the full chapter plan).

This file demonstrates:
- Compiling patterns and using Pattern methods
- search vs findall vs sub
- Greedy vs non-greedy quantifiers
- Simple lookbehind
"""

# Example 1: Search for a pattern
pat_digits = re.compile(r"\d+")
match = pat_digits.search("Age: 25, Height: 180 cm")
if match:
    print(match.group())  # 25

# Example 2: Find all occurrences
pat_three_letters = re.compile(r"\b\w{3}\b")
words = pat_three_letters.findall("The cat is on the mat")
print(words)  # ['The', 'cat', 'on', 'the', 'mat']

# Example 3: Replace pattern in a string
pat_spaces = re.compile(r"\s+")
print(pat_spaces.sub("-", "Hello   World"))  # Hello-World

# Greedy vs. Non-Greedy Matching
pat_tag = re.compile(r"<.*?>")  # non-greedy, stops at first '>'
html = "<div>Hello</div>"
first_tag = pat_tag.search(html)
if first_tag:
    print(first_tag.group())  # <div>

# Lookbehind (fixed-width in Python)
pat_domain = re.compile(r"(?<=@)\w+")
email = "user@example.com"
domain = pat_domain.search(email)
if domain:
    print(domain.group())  # example

# Performance tip: compile patterns used in loops
pat_word = re.compile(r"\w+")
texts = ["one", "two 22", "three"]
for t in texts:
    _ = pat_word.search(t)

