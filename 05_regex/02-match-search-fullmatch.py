import re

"""Demonstrate match vs fullmatch vs search.

- match: only at start of string
- fullmatch: match must consume entire string
- search: anywhere in string
"""

pattern = re.compile(r"foo")

print(bool(pattern.match("foobar")))      # True: starts with 'foo'
print(bool(pattern.fullmatch("foobar")))  # False: not entire string
print(bool(pattern.search("barfoo")))     # True: found inside

# Often you want to validate whole string
hex_color = re.compile(r"#[0-9a-fA-F]{6}")
print(bool(hex_color.fullmatch("#A0B1C2")))   # True
print(bool(hex_color.match("#A0B1C2xx")))     # True, but not a full validation

# Anchors ^ and $ can be combined with search, but fullmatch is simpler
line = "value=42"
print(bool(re.compile(r"^value=\d+$").search(line)))  # True
print(bool(re.compile(r"^value=\d+$").fullmatch(line)))  # True
