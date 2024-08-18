"""https://www.codewars.com/kata/56b5afb4ed1f6d5fb0000991"""

from solution_reverse_or_rotate import rev_rot


def test_example():
    assert rev_rot("1234", 0) == ""
    assert rev_rot("", 0) == ""
    assert rev_rot("1234", 5) == ""
    assert rev_rot("733049910872815764", 5) == "330479108928157"
