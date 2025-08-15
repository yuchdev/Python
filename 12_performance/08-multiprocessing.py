"""CPU-bound work with ProcessPoolExecutor.

Demonstrates bypassing GIL for CPU-bound tasks using multiple processes.
"""

import math
import time
from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(n: int) -> int:
    # Intentionally heavy function
    s = 0
    for i in range(1, n):
        s += int(math.sqrt(i))
    return s


def serial(total: int, n: int) -> float:
    t0 = time.perf_counter()
    for _ in range(total):
        cpu_heavy(n)
    return time.perf_counter() - t0


def parallel(total: int, n: int, workers: int) -> float:
    t0 = time.perf_counter()
    with ProcessPoolExecutor(max_workers=workers) as ex:
        list(ex.map(cpu_heavy, [n] * total))
    return time.perf_counter() - t0


if __name__ == "__main__":
    total, n = 4, 200_000
    print("serial secs:", serial(total, n))
    print("parallel secs:", parallel(total, n, workers=4))