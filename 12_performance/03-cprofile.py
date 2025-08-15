"""Using cProfile to find hotspots.

Run this script directly to see profiling output.
"""

import cProfile
import pstats
import io


def slow_work(n: int) -> int:
    # Synthetic nested loops to profile
    s = 0
    for i in range(n):
        for j in range(50):
            s += (i * j) % 7
    return s


pr = cProfile.Profile()
pr.enable()
result = slow_work(2000)
pr.disable()

s = io.StringIO()
ps = pstats.Stats(pr, stream=s).sort_stats("cumtime")
ps.print_stats(10)
print("result:", result)
print(s.getvalue())
