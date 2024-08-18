"""https://www.codewars.com/kata/526dbd6c8c0eb53254000110"""

import pytest

from solution_not_very_secure import alphanumeric


@pytest.mark.parametrize('s, b', [
    ("hello world_", False),
    ("PassW0rd", True),
    ("     ", False)
])
def test_example(s, b):
    assert alphanumeric(s) == b
