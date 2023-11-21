import unittest
from testing import rle

__doc__ = """
Python.unittest
* Simple unit testing library
* API reminds of Java's JUnit
* Runs all tests in the current directory and subdirectories:
    python -m unittest
* Runs all tests in the specified file:
    python -m unittest tests.py
* Runs all tests in the specified class:
    python -m unittest tests.py TestRle
* Runs specific test:
    python -m unittest tests.py TestRle.test_rle
* `assertEqual` is a method of TestCase class, which can be considered an assert with additional information
* Functions `setUp` and `tearDown` are called before and after each test
* It can be used for creating temporary files, databases, etc.
* Problem with setUp/tearDown is bad composition, that is different tests can affect each other,
  they may require different setUp/tearDown, etc.
"""


# 05. Python.unittest
# Simple unit testing framework
class TestRle(unittest.TestCase):
    def test_rle(self):
        self.assertEqual(list(rle('AABBB')), [('A', 2), ('B', 3)], 'Wrong result')

    def test_rle_empty(self):
        self.assertEqual(list(rle('')), [], 'Wrong result')
