"""Small timing demo and core performance tips.

- Use builtins (often in C) over manual Python loops when possible
- Measure with time.perf_counter() or timeit for micro-benchmarks
- Prefer sets/dicts for membership and lookups
- Consider generators to reduce memory footprint
- Use caching for pure functions when appropriate
"""

import time
from functools import lru_cache

# Builtins vs manual loops
N = 1_000_00  # 100k
nums = list(range(1000)) * 100

start = time.perf_counter()
manual = 0
for x in nums:
    manual += x
print("manual sum:", manual, "secs:", time.perf_counter() - start)

start = time.perf_counter()
builtin_sum = sum(nums)
print("builtin sum:", builtin_sum, "secs:", time.perf_counter() - start)

# Sets for membership
hay = list(range(10_000))
needles = [123, 9999, -1]
start = time.perf_counter()
_ = [n in hay for n in needles]
print("list membership secs:", time.perf_counter() - start)

hay_set = set(hay)
start = time.perf_counter()
_ = [n in hay_set for n in needles]
print("set membership secs:", time.perf_counter() - start)

# Generators vs list (memory-friendly streaming)
# This generator simulates streaming processing

def gen_process(it):
    for i in it:
        yield i * 2

# Caching a pure function (demonstration)
@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

start = time.perf_counter()
print("fib(32)=", fib(32))
print("first call secs:", time.perf_counter() - start)

start = time.perf_counter()
print("fib(32) again=", fib(32))
print("cached call secs:", time.perf_counter() - start)
