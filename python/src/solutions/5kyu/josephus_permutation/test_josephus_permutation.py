"""https://www.codewars.com/kata/5550d638a99ddb113e0000a2"""

from solution_josephus_permutation import *


def test_example_tests__should_work_for_example_tests():
    assert josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2) == [2, 4, 6, 8, 10, 3, 7, 1, 9, 5]
    assert josephus(['C', 'o', 'd', 'e', 'W', 'a', 'r', 's'], 4) == ['e', 's', 'W', 'o', 'C', 'd', 'r', 'a']
    assert josephus([1, 2, 3, 4, 5, 6, 7], 3) == [3, 6, 2, 7, 5, 1, 4]
    assert josephus([], 3) == []
