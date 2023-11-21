import heapq
import random
import time
from enum import Enum, auto
from types import coroutine

__doc__ = """In Python normal generators used for iterations
but can be used for coroutines as well.
Since we don't want to use one thing for 2 purposes, since Python 3.5 we have async/await syntax

These are 2 keywords that can be used in 2 different contexts:
1. async def - defines a coroutine
2. await - yields control to another coroutine

As you see, it's quite similar to generators, but with different keywords
Coroutine does not use __next__() method, but send() instead

We can utilize decorator @types.coroutine to make generator a coroutine
Let's modify example from 09_async/03-state-machine.py
Add @coroutine decorator to waiting() function
Make launch_rocket() a coroutine

Notice that if you call generator or coroutine, it does not start execution
You need to call next() or send() to start execution
The difference is generator does not give any diagnostic if you call it directly,
but coroutine raises TypeError

Performance:
real         0.45
user         0.11
sys          0.03
"""


class State(Enum):
    """
    Enum class for all possible states
    """
    WAITING = 1
    COUNTDOWN = 2
    LAUNCHED = 3


class Event(Enum):
    """
    Enum.auto() is a shortcut for enum incrementation
    """
    WAIT = auto()
    STOP = auto()


def random_delay():
    """
    Return a tuple of delay and countdown
    randrange() has open interval, which is more intuitive
    :return:
    """
    return random.random() * 5, random.randrange(5)


@coroutine
def waiting(delay):
    yield Event.WAIT, delay


async def launch_rocket(delay, countdown):
    """
    Every yield is a state transition
    This function is a generator that corresponds to
    a state machine Launch from 02-state-machine.py
    """
    # State WAITING
    await waiting(delay)
    # State COUNTDOWN
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        await waiting(1)
    # State LAUNCHED
    print("Rocket launched")


start = time.time()
rockets = [(delay, countdown) for delay, countdown in [random_delay() for _ in range(1000)]]
work = [
    (start, rocket_id, launch_rocket(delay, countdown)) for rocket_id, (delay, countdown) in enumerate(rockets)
]
# The main loop almost without changes from 02-state-machine.py
# We replace Launch.step() with launch.send(None)
# Enums are not class attributes anymore
while work:
    step_at, rocket_id, launch = heapq.heappop(work)
    wait = step_at - time.time()
    if wait > 0:
        time.sleep(wait)
    try:
        event, argument = launch.send(None)
    except StopIteration:
        continue
    if event is Event.WAIT:
        step_at = time.time()
        heapq.heappush(work, (step_at, rocket_id, launch))
        print(f"Rocket #{rocket_id + 1} launch in {argument:.2f} seconds")
    else:
        assert event is Event.STOP
        print(f"Rocket #{rocket_id + 1} finished")
