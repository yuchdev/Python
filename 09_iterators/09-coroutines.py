import sys

__doc__ = """Coroutines in Python are functions that can suspend their execution before reaching return, 
and later resume from the same point, possibly with a different context.

The yield keyword is used in coroutines not only to yield a value (produce), 
but also to receive a value (consume) through the generator. 
This bidirectional communication makes coroutines suitable for scenarios
where data needs to flow in both directions.
You can send data to a coroutine using the send() method, and throw exceptions into it using the throw() method

Synchronous Coroutines:
Synchronous coroutines are traditional coroutines that operate in a single-threaded, blocking manner. 
They do not involve asynchronous I/O operations or cooperative multitasking. 
These coroutines are used in a linear, blocking fashion and are suitable for tasks 
that don't require asynchronous I/O handling.

Asynchronous Coroutines:
Asynchronous coroutines are defined with the async def syntax and are designed 
for use in asynchronous programming.
They can perform I/O operations or other tasks that may block without blocking the entire program. 
Asynchronous coroutines can yield control back to an event loop, allowing other tasks to run concurrently. 
They are used in asynchronous frameworks such as asyncio for non-blocking I/O operations.

`yield` can be used for implementing finite state machines.
Every state matched a code between two yield statements.
"""


# TODO: for x in ... yield
# TODO: async with ...

def simple_coroutine():
    """
    Simple synchronous coroutine
    """
    print("Coroutine started")
    received_value = yield 42
    print("Received:", received_value)


def show_simple_coroutine():
    coro = simple_coroutine()
    print("Starts the coroutine")
    next(coro)
    print("Send a value to the coroutine")
    coro.send("Hello, Coroutine")


async def simple_async_coroutine():
    """
    Simple asynchronous coroutine
    """
    print("Coroutine started")
    received_value = yield 42
    print("Received:", received_value)


def show_async_coroutine():
    coro = simple_coroutine()
    print("Starts the coroutine")
    next(coro)
    print("Send a value to the coroutine")
    coro.send("Hello, Coroutine")


async def two_way_coroutine():
    while True:
        received_value = yield
        print("Received:", received_value)
        response = yield "Thank you for " + received_value
        print("Response:", response)


def show_two_way_coroutine():
    coro = two_way_coroutine()
    # Starts the coroutine
    next(coro)
    coro.send("coffee")
    print(coro.send("the coffee"))


async def consumer():
    while True:
        data = yield
        print("Consumed:", data)


def show_consumer():
    coro = consumer()
    next(coro)
    coro.send("Apple")
    coro.send("Banana")


async def data_processor():
    while True:
        data = yield
        processed_data = data.upper()
        yield processed_data


def show_data_processor():
    coro = data_processor()
    next(coro)
    coro.send("apple")
    print(coro.send("banana"))


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
