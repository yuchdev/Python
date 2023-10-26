import random
import sys
import time
import heapq
from enum import Enum, auto

__doc__ = """When we launch huge number of threads with delays, 
we may want to poll the status of each thread. This can be done by using a finite state machine.
In case of the rocket launcher from previous example,
we know the delay and countdown of each rocket,
so we can calculate the expected time of each state.

Performance:
time -lp python3 02-state-machine.py rockets_threading > /dev/null 
real         5.17
user         0.14
sys          0.07

As we see, it's faster than the previous example, because we don't have to wait
but rather perform step and move on

RAM consumption is also lower.

We can much simplify code of FSM using generators
"""


def random_delay():
    """
    Return a tuple of delay and countdown
    randrange() has open interval, which is more intuitive
    :return:
    """
    return random.random() * 5, random.randrange(5)


class Launch:
    """
    Class implementing a finite state machine
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

    def __init__(self, delay, countdown):
        self.delay = delay
        self.countdown = countdown
        self.state = self.State.WAITING

    def step(self):
        """
        Advance the state machine by one step
        Return pair of operation and argument of the operation
        We implement 'if' rather than 'elif' because we can switch state during the step
        """
        if self.state is self.State.WAITING:
            self.state = self.State.COUNTDOWN
            return self.Event.WAIT, self.delay
        if self.state is self.State.COUNTDOWN:
            if self.countdown == 0:
                self.state = self.State.LAUNCHED
            else:
                print(f"{self.countdown}...")
                self.countdown -= 1
                return self.Event.WAIT, 1
        if self.state is self.State.LAUNCHED:
            print("Rocket launched")
            return self.Event.STOP, None

        raise ValueError(f"Unknown state {self.state}")


def rockets_fsm():
    # Assume we want to launch 1000 rockets at the same time
    rockets = [(delay, countdown) for delay, countdown in [random_delay() for _ in range(1000)]]
    start = time.time()
    # Create a list of Launch objects where `i` plays role of rocket id
    # `array` list is sorted on each step, so we can use it as a priority queue
    work = [
        (start, rocket_id, Launch(delay, countdown)) for rocket_id, (delay, countdown) in enumerate(rockets)
    ]
    while work:
        step_at, rocket_id, launch = heapq.heappop(work)
        wait = step_at - time.time()
        if wait > 0:
            time.sleep(wait)
        event, argument = launch.step()
        if event is launch.Event.WAIT:
            step_at = time.time()
            heapq.heappush(work, (step_at, rocket_id, launch))
            step_at = time.time() + argument
            print(f"Rocket #{rocket_id + 1} launch in {argument:.2f} seconds")
            heapq.heappush(work, (step_at, rocket_id, launch))
        else:
            assert event is launch.Event.STOP
            print(f"Rocket #{rocket_id + 1} finished")


if __name__ == '__main__':
    """
    Choose one of examples
    """
    function = sys.argv[1]
    try:
        locals()[function]()
    except KeyError as _:
        print("Choose one of module functions to call, e.g. create")
