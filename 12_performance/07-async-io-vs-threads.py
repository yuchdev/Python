"""Async I/O vs threads for I/O-bound simulated tasks.

Note: We simulate I/O using sleep. Real-world performance depends on workload.
"""

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def io_blocking(delay: float) -> float:
    time.sleep(delay)
    return delay


async def io_async(delay: float) -> float:
    await asyncio.sleep(delay)
    return delay


async def run_async(n: int, delay: float) -> float:
    t0 = time.perf_counter()
    await asyncio.gather(*(io_async(delay) for _ in range(n)))
    return time.perf_counter() - t0


def run_threads(n: int, delay: float) -> float:
    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=n) as ex:
        list(ex.map(io_blocking, [delay] * n))
    return time.perf_counter() - t0


if __name__ == "__main__":
    n, d = 10, 0.05
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    async_time = loop.run_until_complete(run_async(n, d))
    thread_time = run_threads(n, d)
    print("asyncio gather secs:", async_time)
    print("thread pool secs:", thread_time)
