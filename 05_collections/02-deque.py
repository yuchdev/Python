from collections import deque

__doc__ = """Deque is a double-ended queue that allows for efficient and fast appending
and popping elements from both ends.
Deque are implemented in the collections module as the deque class.

Deque is implemented as a doubly linked list of blocks 64 elements long (like in C++), 
which is optimized for fast appends and pops from both ends.
It is more memory efficient because we have logarithmic number of allocations

Index access is O(n) for deque
"""

d = deque(maxlen=3)
# append and appendleft
d.append(1)
d.appendleft(2)
d.append(3)
print(d)

# if you exceed the maxlen, the oldest element will be removed
d.append(4)
print(d)

# pop and popleft
d.pop()
d.popleft()
print(d)

# extend and extendleft
d.extend([4, 5, 6])
d.extendleft([7, 8, 9])
print(d)

# rotate right
d.rotate(3)
print(d)

# rotate left
d.rotate(-3)
print(d)

# insert
d.insert(2, 10)
print(d)
