import re

"""finditer vs findall; split with captures; sub/subn with callable replacement."""

text = "ID=12; ID=345; ID=7"

# finditer yields Match objects lazily (efficient for large texts)
for m in re.finditer(r"\bID=(\d+)\b", text):
    print("id:", m.group(1), "at", m.span(1))

# split: capturing groups are also returned in result
parts = re.split(r"[,;]\s*", "a, b; c, d")
print(parts)  # ['a', 'b', 'c', 'd']

# sub with callable: normalize phone format
phone = "+1 555-123-4567"
pat = re.compile(r"\+?(\d{1,3})[\s-]?(\d{3})[\s-]?(\d{3})[\s-]?(\d{4})")

def repl(m: re.Match) -> str:
    cc, a, b, c = m.groups()
    return f"+{cc} ({a}) {b}-{c}"

print(pat.sub(repl, phone))  # +1 (555) 123-4567

# subn returns (new_string, count)
print(pat.subn(repl, "Call +1 5551234567 or +44 207 123 4567"))
