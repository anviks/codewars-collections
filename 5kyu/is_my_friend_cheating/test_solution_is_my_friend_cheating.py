"""https://www.codewars.com/kata/5547cc7dcad755e480000004"""

import unittest

from solution_is_my_friend_cheating import remov_nb


class CheatingFriend(unittest.TestCase):
    def run_test(self, n, exp):
        actual = remov_nb(n)
        self.assertEqual(actual, exp)

    def test_fixed_tests(self):
        self.run_test(26, [(15, 21), (21, 15)])
        self.run_test(100, [])
        self.run_test(101, [(55, 91), (91, 55)])
