import re
import unicodedata as ud

"""Unicode-aware regex and bytes patterns.

- Python's re is Unicode by default for str patterns
- Use re.ASCII to restrict \w, \d, \s, \b to ASCII
- For binary data, use bytes patterns and inputs
- Normalize text when canonical equivalence matters
"""

# Unicode word characters example
s = "café cafe\u0301"  # composed 'é' and decomposed 'e' + combining acute
pat_word = re.compile(r"café")
print(bool(pat_word.search(s)))  # True for first, not second part

# Normalize to NFC to treat them equivalently
nfc = ud.normalize("NFC", s)
print(bool(pat_word.search(nfc)))  # True

# ASCII flag: \w restricted to ASCII
print(re.findall(r"\w+", "Привет world"))          # ['Привет', 'world']
print(re.findall(r"\w+", "Привет world", re.ASCII))  # ['world']

# Bytes regex: pattern and input must both be bytes
bpat = re.compile(br"\x89PNG\r\n\x1a\n")  # PNG signature
header = b"\x89PNG\r\n\x1a\n......"
print(bool(bpat.match(header)))  # True
