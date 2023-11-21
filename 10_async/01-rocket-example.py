import sys
import time
import random
import threading


__doc__ = """For the initial display of Python threading, imagine we launching a rocket
with function `launch_rocket` and we want to display the countdown on the screen.
`launch_rocket` should accept delay and countdown as arguments, and we generate them randomly.
Let's use Threading to launch 1000 rockets at the same time.

Python Threading API:
* Thread class is copied from Java language, that's why its API looks so odd for Python
* Python threads execute in the same process, so they share the same memory
* Python threads are not preemptive, they can't be interrupted by the system
* Python threads are not parallel, they are executed on the same CPU core

Threading Performance:
* Thread is more lightweight than Process, but it's not always faster
* Every thread address OS kernel to create a new thread, so it's not free
* Every thread has its own stack, which is 1MB on Windows and 8MB on Linux
* If you need computing on multiple CPU cores, use Process
* Python interpreter features mutex called GIL (Global Interpreter Lock)
* GIL blocks any Python thread from executing Python bytecode at the same time

Example:
time -lp python3 01-rocket-example.py rockets_threading > /dev/null
real         9.16
user         0.30
sys          0.23

There are 2 types of bottleneck in parallel programs: CPU and IO
In Pyton we can't deal with CPU bottleneck, but we can deal with IO bottleneck
GIL not so critical for IO operations, because most general-purpose applications wait for IO
"""


def random_delay():
    """
    Return a tuple of delay and countdown
    randrange() has open interval, which is more intuitive
    :return:
    """
    return random.random() * 5, random.randrange(5)


def launch_rocket(delay, countdown):
    time.sleep(delay)
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        time.sleep(1)
    print("Rocket launched")


def rockets_serial():
    """
    Launch 1000 rockets by one
    """
    rockets = [(delay, countdown) for delay, countdown in [random_delay() for _ in range(1000)]]
    for i, (delay, countdown) in enumerate(rockets):
        print(f"Rocket #{i + 1} launch in {delay:.2f} seconds with countdown {countdown}")
        launch_rocket(delay, countdown)


def rockets_threading():
    """
    Assume we want to launch 1000 rockets at the same time
    Thread class is copied from Java language, that's why its API looks so odd for Python
    We generate all threads first, then start them, then wait for them to finish
    We don't join in a cycle because it will block the main thread
    """
    rockets = [(delay, countdown) for delay, countdown in [random_delay() for _ in range(1000)]]
    threads = [threading.Thread(target=launch_rocket, args=(delay, countdown)) for delay, countdown in rockets]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


# Nore: launch rockets_threading() with redirecting output to /dev/null
# in order to measure the performance without IO operations
# You can also use `time` command to measure the performance:
# time python 01-rocket-example.py rockets_threading > /dev/null
if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
