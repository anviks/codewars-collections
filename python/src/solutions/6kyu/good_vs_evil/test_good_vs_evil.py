"""https://www.codewars.com/kata/52761ee4cffbc69732000738"""

from solution_good_vs_evil import *


def test_sample_tests():
    assert good_vs_evil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good'
    assert good_vs_evil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil'
    assert good_vs_evil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field'
