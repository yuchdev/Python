import re
import time

"""Performance tips: precompilation, specific patterns, and simple timing.

Note: Python 3.11+ adds timeout= to some APIs like re.compile and re.search; if unavailable,
avoid pathological patterns and consider external timeouts.
"""

texts = ["a" * 1000 + "!" for _ in range(1000)]

# Pathological/backtracking-prone vs specific
bad = re.compile(r"(a+)+!")
good = re.compile(r"a+!")

start = time.perf_counter()
s1 = sum(bool(bad.search(t)) for t in texts)
print("bad pattern secs:", time.perf_counter() - start, s1)

start = time.perf_counter()
s2 = sum(bool(good.search(t)) for t in texts)
print("good pattern secs:", time.perf_counter() - start, s2)

# Pre-compile once and reuse in a loop
pat_word = re.compile(r"\w+")
start = time.perf_counter()
for t in texts:
    pat_word.search(t)
print("compiled search secs:", time.perf_counter() - start)

start = time.perf_counter()
for t in texts:
    re.search(r"\w+", t)
print("module-level search secs:", time.perf_counter() - start)
