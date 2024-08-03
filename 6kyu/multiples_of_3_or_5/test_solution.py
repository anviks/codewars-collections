"""https://www.codewars.com/kata/514b92a657cdc65150000006"""

import unittest

from solution import solution


class SampleTests(unittest.TestCase):
    def test_should_return_3_for_n_4(self):
        self.assertEqual(solution(4), 3)

    def test_should_return_8_for_n_6(self):
        self.assertEqual(solution(6), 8)

    def test_should_return_60_for_n_16(self):
        self.assertEqual(solution(16), 60)

    def test_should_return_0_for_n_3(self):
        self.assertEqual(solution(3), 0)

    def test_should_return_3_for_n_5(self):
        self.assertEqual(solution(5), 3)

    def test_should_return_45_for_n_15(self):
        self.assertEqual(solution(15), 45)

    def test_should_return_0_for_n_0(self):
        self.assertEqual(solution(0), 0)

    def test_should_return_0_for_n_1(self):
        self.assertEqual(solution(-1), 0)

    def test_should_return_23_for_n_10(self):
        self.assertEqual(solution(10), 23)

    def test_should_return_78_for_n_20(self):
        self.assertEqual(solution(20), 78)

    def test_should_return_9168_for_n_200(self):
        self.assertEqual(solution(200), 9168)
