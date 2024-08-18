"""https://www.codewars.com/kata/57b06f90e298a7b53d000a86"""

from solution_the_supermarket_queue import *


def test_the_supermarket_queue__examples():
    assert queue_time([], 1) == 0, 'wrong answer for case with an empty queue'
    assert queue_time([5], 1) == 5, 'wrong answer for a single person in the queue'
    assert queue_time([2], 5) == 2, 'wrong answer for a single person in the queue'
    assert queue_time([1, 2, 3, 4, 5], 1) == 15, 'wrong answer for a single till'
    assert queue_time([1, 2, 3, 4, 5], 100) == 5, 'wrong answer for a case with a large number of tills'
    assert queue_time([2, 2, 3, 3, 4, 4], 2) == 9, 'wrong answer for a case with two tills'
