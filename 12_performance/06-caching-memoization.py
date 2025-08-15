"""Caching with functools.lru_cache."""

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def ack(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))

start = time.perf_counter()
print(ack(2, 10))
print("first call secs:", time.perf_counter() - start)

start = time.perf_counter()
print(ack(2, 10))
print("cached secs:", time.perf_counter() - start)
