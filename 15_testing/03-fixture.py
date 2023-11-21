import pytest

__doc__ = """Fixtures are a way to provide data to tests.
It provides the same functionality as setUp/tearDown, but in a more flexible way
Fixture is a decorator
"""


@pytest.fixture
def tempfile(tmpdir):
    """
    Creates a temporary file and returns its name
    """
    file = tmpdir.join('tempfile')
    file.write('Hello world!')
    return file
