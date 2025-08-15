"""Generators vs lists: memory and throughput trade-offs."""

import sys

# A generator that yields numbers up to n
def gen(n):
    for i in range(n):
        yield i * 2

# A list that materializes numbers up to n
def make_list(n):
    return [i * 2 for i in range(n)]

n = 1_00000  # 100k
g = gen(n)
lst = make_list(n)

print("gen size (iterator object):", sys.getsizeof(g))
print("list size (elements materialized):", sys.getsizeof(lst))

# Use the generator in a pipeline
print(sum(gen(n)))
