"""https://www.codewars.com/kata/58235a167a8cb37e1a0000db"""

from solution_pair_of_gloves import *


def test_basic_tests__basic_tests():
    assert number_of_pairs(['red', 'red']) == 1
    assert number_of_pairs(['red', 'green', 'blue']) == 0
    assert number_of_pairs(['gray', 'black', 'purple', 'purple', 'gray', 'black']) == 3
    assert number_of_pairs([]) == 0
    assert number_of_pairs(['red', 'green', 'blue', 'blue', 'red', 'green', 'red', 'red', 'red']) == 4
