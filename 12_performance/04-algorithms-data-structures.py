"""Algorithms and data structures choices matter.

- List vs set membership
- Dict lookups
- heapq for priority queues
"""

import time
import heapq

# Membership
hay = list(range(50_000))
needles = list(range(-100, 100))

start = time.perf_counter()
_ = [n in hay for n in needles]
print("list membership secs:", time.perf_counter() - start)

hay_set = set(hay)
start = time.perf_counter()
_ = [n in hay_set for n in needles]
print("set membership secs:", time.perf_counter() - start)

# Dict lookups
phone = {f"user{i}": i for i in range(100_00)}
start = time.perf_counter()
_ = [phone.get("user9999") for _ in range(100_00)]
print("dict get secs:", time.perf_counter() - start)

# heapq
nums = [5, 2, 9, 1, 5, 6]
heapq.heapify(nums)
heapq.heappush(nums, 3)
print("smallest:", heapq.heappop(nums))
