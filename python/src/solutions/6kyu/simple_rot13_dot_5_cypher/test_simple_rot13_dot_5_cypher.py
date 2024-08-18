"""https://www.codewars.com/kata/5894986e2ddc8f6805000036"""

from solution_simple_rot13_dot_5_cypher import *


def test_fixed_tests__basic_test_cases():
    assert rot_135('The quick brown fox jumps over the 2 lazy dogs') == 'Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf'
    assert rot_135('Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf') == 'The quick brown fox jumps over the 2 lazy dogs'
