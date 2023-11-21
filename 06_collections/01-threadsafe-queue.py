import sys
import threading
from queue import Queue

__doc__ = """Queue is designed to be thread-safe
"""

# Create a Queue with a maximum size of 10
q = Queue(maxsize=10)


# Define a function to add items to the queue
def producer():
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")


# Define a function to remove items from the queue
def consumer():
    while not q.empty():
        item = q.get()
        print(f"Consumed: {item}")


def show_queue():

    # Create producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    # Start the threads
    producer_thread.start()
    consumer_thread.start()

    # Wait for the threads to finish
    producer_thread.join()
    consumer_thread.join()


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of functions to call")
