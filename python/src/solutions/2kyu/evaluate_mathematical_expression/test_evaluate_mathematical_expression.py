"""https://www.codewars.com/kata/52a78825cdfc2cfc87000005"""

import pytest

from solution_evaluate_mathematical_expression import calc


@pytest.mark.parametrize('expression, expected', [
    ("1 + 1", 2),
    ("8/16", 0.5),
    ("3 -(-1)", 4),
    ("2 + -2", 0),
    ("10- 2- -5", 13),
    ("(((10)))", 10),
    ("3 * 5", 15),
    ("-7 * -(6 / 3)", 14),
    ("74 + -22 - -33 - 91 * 63 * -45 - -76 * 86", 264606),
    ("(-74) / (47 + 6 * (8)) + (-48 * (((-(93 / -91)))) + 29)", -20.833892423366105),
    ("-(-35) + (19 * 58 - -(72)) - (47 + -(((-(-98 / -79)))) * -7)", 1170.6835443037974),
])
def test_example(expression, expected):
    assert calc(expression) == expected
