import sys
from queue import PriorityQueue
import heapq

__doc__ = """PriorityQueue in Python is built on top of the heapq module and implements a min-priority queue.
heapq offers several functions:
heapq.heappush(heap, item) - Push the value item onto the heap, maintaining the heap invariant.
heapq.heappop(heap) - Pop and return the smallest item from the heap, maintaining the heap invariant.
heapq.heapify(x) - Transform list x into a heap, in-place, in linear time.
heapq.heapreplace(heap, item) - Pop and return the smallest item from the heap, and also push the new item.
heapq.merge(*iterables, key=None, reverse=False) - Merge multiple sorted inputs into a single sorted output

We implement merge() within the heapq module heapq, because merge() uses a heap internally 
"""


def show_pq():
    # put and pop
    pq = PriorityQueue()
    pq.put((1, 'a'))
    pq.put((3, 'b'))
    pq.put((2, 'c'))
    print(pq)
    while not pq.empty():
        print(pq.get())


def show_heapq():
    # heapify, heappop and heappush
    data = [(1, 'a'), (3, 'b'), (2, 'c')]
    heapq.heapify(data)
    print(data)

    heapq.heappush(data, (4, 'd'))
    while len(data):
        print(heapq.heappop(data))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
