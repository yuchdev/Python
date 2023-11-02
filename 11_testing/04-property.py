import random
from hypothesis import given, strategies as st
from itertools import tee, chain, repeat
from testing import sort, rle

__doc__ = """Property-based testing is a way to test code with random data
Sometimes we generate completely random data, however most of the time we need dataset with specific properties
E.g. QuickSort is a sorting algorithm which is extremely ineffective on sorted data

Framework Hypothesis is a way to test code with random data
* Hypothesis works by generating random data and checking if the property holds
* Strategy is a way to generate random data
* Strategies can be combined
* All failed tests are saved for further investigation
"""


def is_sorted(iterable):
    """
    Checks if iterable is sorted
    """
    return all(a <= b for a, b in zip(iterable, iterable[1:]))


def check_sort(iterable):
    """
    Checks if iterable is sorted
    """
    copy_iterable = iterable[:]
    sort(copy_iterable)
    assert is_sorted(copy_iterable), f'{copy_iterable} is not sorted'


def random_list():
    """
    Generates random list
    """
    return random.choices(range(100), k=10)


def random_almost_sorted():
    """
    Generates almost sorted list
    """
    sorted_list = random_list()
    sorted_list.sort()
    # replace several elements with random ones
    for _ in range(3):
        sorted_list[random.randint(0, len(sorted_list) - 1)] = random.randint(0, 100)
    return sorted_list


def random_reversed():
    """
    Generates reversed list
    """
    return random_list().sort(reverse=True)


test_list = random_list()
sort(test_list)
assert is_sorted(test_list), f'{test_list} is not sorted'

test_almost_sorted = random_almost_sorted()
sort(test_almost_sorted)
assert is_sorted(test_almost_sorted), f'{test_almost_sorted} is not sorted'


@given(st.lists(st.integers()))
def test_sort_random(iterable):
    """
    Tests sort with random data
    """
    check_sort(iterable)


# Let's test our rle function
iterables = st.one_of(st.tuples(st.integers()),
                      st.lists(st.integers()),
                      st.text().map(iter))


@given(iterables)
def test_rle(it):
    """
    Tests rle function
    Run:
    python3 -m pytest 04-property.py
    """
    def encode_decode(it2):
        return chain.from_iterable(repeat(x, n) for x, n in rle(it2))
    it, it_copy = tee(it)
    expected = list(it_copy)
    actual = list(encode_decode(it))
    assert expected == actual, f'{expected} != {actual}'


@st.composite
def almost_sorted_lists(draw):
    """
    Define a strategy for almost sorted lists
    """
    size = draw(st.integers(min_value=0, max_value=100))  # Define the size of the list
    sorted_list = sorted(range(size))  # Create a sorted list
    num_swaps = draw(st.integers(min_value=0, max_value=size // 2))  # Number of swaps

    for _ in range(num_swaps):
        # Perform swaps to make the list almost sorted
        index1 = draw(st.integers(min_value=0, max_value=size - 1))
        index2 = draw(st.integers(min_value=0, max_value=size - 1))
        sorted_list[index1], sorted_list[index2] = sorted_list[index2], sorted_list[index1]

    return sorted_list


# Use the custom strategy in a test
@given(almost_sorted_lists())
def test_almost_sorted_list(almost_sorted_list):
    almost_sorted_dataset = almost_sorted_list[:]
    sort(almost_sorted_dataset)
    assert is_sorted(almost_sorted_dataset), f'{almost_sorted_dataset} is not sorted'
