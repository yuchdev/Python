import re

"""Flags: IGNORECASE, MULTILINE, DOTALL, VERBOSE and inline flags."""

text = """Line1
Value: 10
LINE3"""

# MULTILINE: ^ and $ match at line boundaries
pat = re.compile(r"^value: \d+$", flags=re.IGNORECASE | re.MULTILINE)
print(bool(pat.search(text)))  # True

# DOTALL: dot matches newlines
pat2 = re.compile(r"Line1.*LINE3", flags=re.DOTALL)
print(bool(pat2.search(text)))  # True

# VERBOSE: whitespace/comments inside pattern are ignored
phone_verbose = re.compile(
    r"""
    \+?            # optional plus
    (?:\d{1,3})?   # optional country code
    [\s-]?         # optional separator
    (\d{3})        # area
    [\s-]?
    (\d{3})
    [\s-]?
    (\d{4})
    """,
    re.VERBOSE,
)
print(bool(phone_verbose.fullmatch("+1 555-123-4567")))  # True

# Inline flags
print(bool(re.search(r"(?im)^value: \d+$", text)))  # (?i)(?m) inline
