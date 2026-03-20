# Chapter 7. Additional Collections

This chapter covers specialized collection data types in Python's `collections` and `queue` modules, providing alternatives to the built-in `dict`, `list`, `set`, and `tuple`.

## The `collections` Module
* **`deque` (Double-Ended Queue)**: Optimized for fast $O(1)$ appends and pops from both ends. It has a `maxlen` attribute to create a bounded buffer. Implemented as a doubly linked list of blocks.
* **`namedtuple`**: Creates tuple subclasses with named fields. Memory efficient like a tuple but readable like an object. Can be subclassed to add methods.
* **`defaultdict`**: A dictionary subclass that calls a factory function to provide missing values (e.g., `defaultdict(list)`).
* **`Counter`**: A dictionary subclass for counting hashable objects. Supports set-like mathematical operations (addition, subtraction, intersection).
* **`OrderedDict`**: A dictionary subclass that remembers the order in which items were added (standard `dict` also does this since Python 3.7, but `OrderedDict` has specific methods like `move_to_end`).
* **`ChainMap`**: Groups multiple dictionaries into a single mapping for grouped lookups.

## The `queue` Module (Thread-Safe)
* **`Queue`**: A multi-producer, multi-consumer FIFO queue. Thread-safe and useful for inter-thread communication.
* **`LifoQueue`**: A LIFO (Last-In-First-Out) queue, similar to a stack.
* **`PriorityQueue`**: A thread-safe priority queue. Items are retrieved in order of priority (lowest value first).

## Heaps (`heapq`)
The `heapq` module provides an implementation of the heap queue algorithm (priority queue). It works on standard Python lists.
* `heappush(heap, item)`: Adds an item to the heap.
* `heappop(heap)`: Removes and returns the smallest item.
* `heapify(list)`: Converts a list to a heap in-place in $O(n)$ time.

---
### Examples
* `01-threadsafe-queue.py`: Producer-consumer pattern using `queue.Queue`.
* `02-deque.py`: Using `deque` as a circular buffer with `maxlen`.
* `03-named-tuple.py`: Defining and subclassing `namedtuple` and `typing.NamedTuple`.
* `04-default-dict.py`: Grouping items and using lambdas for default values.
* `05-ordered-dict.py`: Order-sensitive dictionary operations.
* `06-counter.py`: Word counting and `most_common()` elements.
* `07-chain-map.py`: Layering multiple dictionaries for lookups.
* `08-priority-queue.py`: Comparing `queue.PriorityQueue` and `heapq`.
