import heapq
import random
import time
from enum import Enum, auto

__doc__ = """Let's implement FSM using generators
Every yield is a state transition
yield from differs from yield in that it delegates to another generator or iterable
and works with iterators of indefinite length

Let's measure the performance of this approach
time -lp python3 03-state-machine.py
real         1.64
user         0.11
sys          0.04

As we see even better performance than in 02-state-machine.py
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


def waiting(delay):
    yield Event.WAIT, delay


def launch_rocket(delay, countdown):
    """
    Every yield is a state transition
    This function is a generator that corresponds to
    a state machine Launch from 02-state-machine.py
    """
    # State WAITING
    yield from waiting(delay)
    # State COUNTDOWN
    for i in reversed(range(countdown)):
        print(f"{i + 1}...")
        yield from waiting(1)
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
