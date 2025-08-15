"""Micro-benchmarking with timeit and perf_counter.

Notes:
- Always run multiple repeats; results vary across runs and machines
- Be careful with micro-optimizations; prioritize algorithmic improvements
"""

import time
import timeit

setup = "nums = list(range(1000))"
stmt_loop = "s=0\nfor x in nums: s+=x"
stmt_builtin = "sum(nums)"

print("perf_counter demo:")
start = time.perf_counter()
s = 0
for i in range(1_0000):
    s += i
print("elapsed secs:", time.perf_counter() - start)

print("timeit demo (smaller is better):")
print("loop:", timeit.timeit(stmt_loop, setup=setup, number=1000))
print("builtin sum:", timeit.timeit(stmt_builtin, setup=setup, number=1000))
