from testing import rle

__doc__ = """Testing in Python is not a part of language, but it is a part of standard library.
There are no strict guidelines on how to write tests, but there are some best practices.
Some of them are:
* Tests should be isolated from each other
* Test user-visible behavior first
* The best test is integration test without many dependencies
* Integration tests are more effective because they take less changes to break
* Data-driven tests are better than copy-pasted tests
* Less code, more data
* Asynchronous code is very hard to test. Resort to making load/integration tests instead

Let's test some approaches to testing in Python:
Print
Better than nothing, but not good

Assert
* Better than nothing, better than print
* Fits for small scripts
* Do not use in production

Assert with context
* Assert context is additional information about the error
* You can pass not only strings, but also any object
* It's convenient to use the tuple

Doctest is a module for testing docstrings
* It works by running the code in docstring and comparing the result with the expected one
* Problem of doctest is that it's hard to test multiline code
* It general lots of false positives
* Testing code with documentation is not a good practice, because documentation tends to become outdated
* From the other side, it's a good reminder to update documentation
* It can be considered as a tool for testing documentation, not code

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

PyTest
* Simple unit testing framework
* Runs all tests in the current directory and subdirectories:
     python3 -m pytest 01-testing.py
* Instead of family of methods assert*, it uses simple assert
* It has a lot of plugins, for example, pytest-asyncio
* It works by parsing the code, building the AST and running the tests

Fixtures are a way to provide data to tests.
* Provides the same functionality as setUp/tearDown, but in a more flexible way
* Fixture is a decorator
* Support better composition
* Fixtures can be composed with one another
* Pytest provides module-level fixtures
* Lots of built-in fixtures

Other features of Pytest
* Parametrization of fixtures and tests
* Testing exceptions and warnings (e.g. 'deprecated' warnings)
* Marking tests with decorators
* Running tests in parallel
* Running tests in subprocesses
* Testing asyncio code
* 

Mocking: Testing component integration
* Mocking is a way to replace one component with some test implementation
* unittest.mock is a module for mocking, interestingly offers better API, not consistent with unittest
* e.g. email sending, database access, etc.
* Mocks are callable
* Mock returns another mock
* Mock overloads __getattr__ and __call__ in order to replace any component

"""

# Tests

# 01. Just print the result
print(list(rle('AABBB')))

# 02. Assert the result
# Better than nothing, better than print
# Fits for small scripts
# Do not use in production
assert list(rle('AABBB')) == [('A', 2), ('B', 3)]


# 03. Assert with context
# Assert context is additional information about the error
# You can pass not only strings, but also any object
# It's convenient to use the tuple
def test_rle():
    assert list(rle('AABBB')) == [('A', 2), ('B', 3)], ('Wrong result', 'AABBB')


# 04. Doctest


# 05. Python.unittest
# Simple unit testing framework

# 06. Pytest
# Run this test:
# python3 -m pytest 01-testing.py
