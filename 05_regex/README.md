# Chapter 5. Regular Expressions

This chapter focuses on Python-specific usage of regular expressions via the standard re module. It complements prior knowledge of regex syntax by emphasizing Python APIs, Unicode handling, bytes vs str, performance, and common patterns.

### Goals

- Understand Python's re module objects: Pattern and Match
- Choose the right function: match, fullmatch, search, findall, finditer, split, sub, subn
- Use grouping: numbered, named, non-capturing, backreferences
- Learn and combine flags: IGNORECASE, MULTILINE, DOTALL, ASCII, VERBOSE, etc.
- Work correctly with Unicode and bytes
- Apply practical text-processing tasks idiomatically in Python
- Recognize performance pitfalls and mitigation strategies

### Theory (as in Python docs)

- Module re overview and compilation
  - re.compile(pattern, flags=0) returns Pattern
  - Pattern methods vs module-level functions
  - Raw string literals r"..." and escaping in Python strings
- Matching primitives
  - match vs fullmatch vs search
  - findall vs finditer (lists vs iterators, groups result shapes)
  - split and maxsplit; capturing groups in split
  - sub vs subn; callable replacement function signature (def repl(m: Match) -> str)
- Groups and references
  - Capturing groups ( ... ), non-capturing (?: ... ), named groups (?P<name>...)
  - Access: m.group(), m.groups(), m.groupdict(), m["name"], m.start(), m.end(), m.span()
  - Backreferences: \1, (?P=name)
- Flags
  - re.IGNORECASE, re.MULTILINE, re.DOTALL, re.ASCII, re.VERBOSE, re.DEBUG
  - Combining flags with |; flags on compile and inline (?i), (?m), (?s), (?x)
- Lookaround
  - Lookahead (?=...) (?!...), lookbehind (?<=...) (?<!...)
  - Python lookbehind is fixed-width
- Unicode and locales
  - Default behavior is Unicode-aware; \w, \b, casefolding nuances with IGNORECASE
  - re.ASCII to restrict \w, \d, \s to ASCII
  - Normalization note: use unicodedata.normalize before regex when equivalence matters
- Bytes vs str
  - Pattern and input types must match (both bytes or both str)
  - Flags behavior with bytes (e.g., re.ASCII implied for classes)
- Performance and safety
  - Pre-compile patterns used in loops
  - Prefer specific patterns; avoid catastrophic backtracking patterns
  - Use finditer for large inputs; lazy quantifiers when appropriate
  - Python 3.11+ supports timeout= on many APIs; otherwise watchdogs
