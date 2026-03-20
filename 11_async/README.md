# Chapter 11. Asynchronous Programming

This chapter covers Python's asynchronous subsystem, comparing it to traditional threading and exploring the foundations of coroutines and the `asyncio` framework.

## Concurrency Models
* **Threading**: Shared memory, preemptive (from OS perspective), but limited by the **GIL (Global Interpreter Lock)** in Python. Good for blocking I/O but doesn't scale well to thousands of connections due to stack memory overhead.
* **Multiprocessing**: Separate memory, true parallelism. Best for CPU-bound tasks.
* **Asynchronous I/O (asyncio)**: Cooperative multitasking in a single thread. Excellent for high-concurrency I/O-bound tasks.

## Foundations
* **Event Loop**: The core of `asyncio`. It manages and distributes the execution of different tasks.
* **Coroutines**: Functions defined with `async def`. They don't run immediately when called; instead, they return a coroutine object that must be `awaited`.
* **Awaitable Objects**: Any object that can be used in an `await` expression (Coroutines, Tasks, Futures).

## `asyncio` Essentials
* **`asyncio.run(coro)`**: The main entry point to run the top-level coroutine.
* **Tasks**: Wrappers for coroutines that schedule them to run on the event loop. Created with `asyncio.create_task()`.
* **Gathering**: `asyncio.gather(*aws)` runs multiple awaitables concurrently and returns their results as a list.
* **Non-blocking I/O**: Foundations built on the `selectors` module and system calls like `select`, `poll`, or `epoll`.

## Async Networking
`asyncio` provides high-level "streams" for network communication:
* **`asyncio.open_connection(host, port)`**: Returns a `(reader, writer)` pair for a TCP client.
* **`asyncio.start_server(cb, host, port)`**: Starts a TCP server that calls a callback for each new connection.

---
### Examples
* `01-rocket-example.py`: Comparison between serial and threaded rocket launches.
* `02-state-machine.py` & `03-state-machine.py`: Modeling async behavior with manual state machines.
* `04-async.py` & `05-async.py`: Moving from generators to `async/await` syntax.
* `06-net-client.py`: A simple TCP client using `asyncio` streams.
* `07-net-server.py`: A basic synchronous socket server.
* `08-async-server.py`: A server using the low-level `selectors` module.
* `09-async-server2.py`: A modern server implementation using `asyncio.start_server`.
