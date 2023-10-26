import sys
import asyncio

__doc__ = """Async and coroutines properties:
* async for is a shortcut for async iterator
* async with is a shortcut for async context manager
* async def - defines a coroutine
* await - yields control to another coroutine
* @coroutine decorator makes generator a coroutine
* Coroutine does not use __next__() method, but send() instead
* If you call generator or coroutine, it does not start execution
"""


def show_async_for():
    """
    Async for is a shortcut for async iterator
    """
    async def async_generator():
        for i in range(5):
            print("Yielding", i)
            yield i
            await asyncio.sleep(0.1)

    async def main():
        async for i in async_generator():
            print(i)

    asyncio.run(main())


def show_async_with():
    """
    Async with is a shortcut for async context manager
    """
    class AsyncContextManager:
        async def __aenter__(self):
            print("Entering context")
            await asyncio.sleep(0.1)

        async def __aexit__(self, exc_type, exc_val, exc_tb):
            print("Exiting context")
            await asyncio.sleep(0.1)

    async def main():
        async with AsyncContextManager():
            print("Inside context")
    asyncio.run(main())


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
