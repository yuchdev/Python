# Chapter 12. Performance in Python

This chapter focuses on measuring, understanding, and improving the performance of Python code. It covers measurement tools, algorithmic choices, and the impact of Python's memory model and the Global Interpreter Lock (GIL).

## Measurement & Profiling
* **`time.perf_counter()`**: The most precise way to measure duration for a single piece of code.
* **`timeit` module**: Best for micro-benchmarking small snippets.
* **`cProfile`**: A built-in deterministic profiler. Use it to find "hotspots" in your application.
* **`pstats`**: Used to read and format the output of `cProfile`.

## Data Structures & Algorithms
* **Membership Testing**: Searching a `set` or `dict` is $O(1)$, while searching a `list` is $O(n)$.
* **Memory Management**: Use **generators** instead of large list comprehensions to process data in a memory-efficient "streaming" manner.
* **`__slots__`**: Use in classes with many instances to reduce memory overhead by skipping the per-instance `__dict__`.

## Optimization Techniques
* **Built-ins**: Always prefer Python's built-in functions (like `sum()`, `min()`, `max()`) and standard library modules, as they are often implemented in highly optimized C.
* **Caching**: Use `functools.lru_cache` to store the results of expensive pure functions.
* **Vectorization**: For heavy numerical work, use libraries like NumPy that perform operations on entire arrays at once.

## Concurrency & The GIL
* **GIL (Global Interpreter Lock)**: A mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once.
* **Threads vs. Processes**:
    * Use **Threads** for I/O-bound tasks (waiting for network/disk).
    * Use **Multiprocessing** for CPU-bound tasks to bypass the GIL.
* **Free-threaded CPython (Experimental)**: Python 3.13 introduces an experimental build that can run without a GIL (PEP 703), allowing true multi-core execution of Python threads.

---
### Examples
* `01-basics.py`: Simple timing demo, built-ins vs. manual loops, and basic caching.
* `02-timeit-perf_counter.py`: Comparing micro-benchmarking tools.
* `03-cprofile.py`: Profiling a synthetic workload and analyzing the results.
* `04-algorithms-data-structures.py`: Performance impact of choosing the right data structure (List vs. Set).
* `05-generators-vs-lists.py`: Memory usage comparison for large datasets.
* `06-caching-memoization.py`: Using `@lru_cache` to optimize recursive functions.
* `07-async-io-vs-threads.py`: Comparing `asyncio` and `threading` for I/O-bound tasks.
* `08-multiprocessing.py`: Using `ProcessPoolExecutor` for CPU-intensive work.
* `09-free-threaded-model.py`: Experimental GIL-free threading demo (Python 3.13+).
