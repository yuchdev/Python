"""Experimental: Free-threaded CPython (Python 3.13+) threading benchmark

This script demonstrates how CPU-bound threads can scale when the GIL is disabled
in a free-threaded CPython build (PEP 703). On a regular CPython with the GIL,
you should NOT expect a speedup from ThreadPoolExecutor on CPU-bound workloads.

How to try (if your Python supports it):
- Run normally:         python 09-free-threaded-threads.py
- If Python 3.13+ supports toggling the GIL: python -X gil=0 09-free-threaded-threads.py
  (Flag and availability may vary by build. Some builds require configuring/compiling
   CPython with GIL disabled; consult your Python 3.13 docs.)

This script:
- Detects Python version and tries to import the "atomic" module (3.13+),
  falling back gracefully if unavailable.
- Compares serial vs threaded execution of a CPU-heavy function.
- Demonstrates a thread-safe counter using atomic primitives when available.

Safe to run on older Pythons: it will just print guidance and skip atomic demo if needed.
"""

from __future__ import annotations

import math
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

# Try to detect Python 3.13 features
PY_VER = sys.version_info

try:
    # Python 3.13 introduces an experimental atomic module for free-threaded builds
    # API is subject to change; we guard usage.
    import atomic  # type: ignore  # noqa: F401
    HAS_ATOMIC = True
except Exception:
    HAS_ATOMIC = False


def cpu_heavy(n: int) -> int:
    """Intentionally CPU-heavy function (pure Python)."""
    s = 0
    for i in range(1, n):
        s += int(math.sqrt(i))
    return s


def serial(total: int, n: int) -> float:
    t0 = time.perf_counter()
    for _ in range(total):
        cpu_heavy(n)
    return time.perf_counter() - t0


def threaded(total: int, n: int, workers: int) -> float:
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(cpu_heavy, [n] * total))
    return time.perf_counter() - t0


# Optional: show an atomic increment demo if available (3.13+ experimental)

def demo_atomic_increments(iterations: int) -> Optional[int]:
    if not HAS_ATOMIC:
        return None
    try:
        # The proposed API in 3.13 is experimental; one design is atomic.Int.
        # We attempt a conservative usage behind try/except to avoid breakage
        # if the exact API name differs in your build.
        from atomic import Int  # type: ignore
        from threading import Thread

        counter = Int(0)

        def worker(k: int) -> None:
            for _ in range(k):
                # Increment atomically without needing a Lock
                counter.fetch_add(1)

        threads = [Thread(target=worker, args=(iterations,)) for _ in range(4)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return int(counter)
    except Exception as e:
        print("[info] atomic demo unavailable or API mismatch:", e)
        return None


if __name__ == "__main__":
    total, n = 8, 250_000
    workers = min(4, (os.cpu_count() or 2))

    print(f"Python: {sys.version.splitlines()[0]}")
    print(f"OS CPUs: {os.cpu_count()}  | workers: {workers}")

    # Heuristic hint: Some experimental builds expose a -X gil=0 flag.
    # There's no stable public function to query this across all builds; we just inform.
    print("Hint: On a free-threaded CPython 3.13 build, try: python -X gil=0 09-free-threaded-threads.py")

    s = serial(total, n)
    t = threaded(total, n, workers)

    print(f"serial secs:   {s:.4f}")
    print(f"threaded secs: {t:.4f}  (expected speedup only on free-threaded CPython)")

    # Atomic counter demo
    if PY_VER >= (3, 13):
        if HAS_ATOMIC:
            res = demo_atomic_increments(50_000)
            if res is not None:
                print("atomic counter result:", res)
        else:
            print("[info] Python >= 3.13 detected, but 'atomic' module not available in this build.")
    else:
        print("[info] atomic module and free-threaded mode are Python 3.13+ experimental features.")
