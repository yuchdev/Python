import re

"""Capturing groups, named groups, backreferences, and Match API."""

pattern = re.compile(r"(?P<user>[A-Za-z0-9._%+-]+)@(?P<domain>[A-Za-z0-9.-]+)\.(?P<tld>[A-Za-z]{2,})")
text = "Contact us: admin@example.com or support@sub.domain.org"

for m in pattern.finditer(text):
    print(m.group(0), m.group("user"), m.group("domain"), m.group("tld"))
    print(m.groups())           # tuple of captured groups
    print(m.groupdict())        # dict of named groups
    print(m.span("domain"))    # start/end of domain

# Backreference to ensure the same quote is used around a value
quoted = re.compile(r"([\"'])value=\d+\1")
print(bool(quoted.fullmatch("'value=10'")))  # True
print(bool(quoted.fullmatch('"value=10"')))  # True
print(bool(quoted.fullmatch("'value=10\"")))  # False
