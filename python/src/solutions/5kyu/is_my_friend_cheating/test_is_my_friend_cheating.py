"""https://www.codewars.com/kata/5547cc7dcad755e480000004"""

from solution_is_my_friend_cheating import *


def run_test(n, exp):
    actual = remov_nb(n)
    assert actual == exp


def test_cheating_friend__fixed_tests():
    run_test(26, [(15, 21), (21, 15)])
    run_test(100, [])
    run_test(101, [(55, 91), (91, 55)])
