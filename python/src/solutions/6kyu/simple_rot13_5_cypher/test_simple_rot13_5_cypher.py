"""https://www.codewars.com/kata/5894986e2ddc8f6805000036"""

import unittest

from solution_simple_rot13_5_cypher import rot_135


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(rot_135("The quick brown fox jumps over the 2 lazy dogs"),
                         "Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf")
        self.assertEqual(rot_135("Gur dhvpx oebja sbk whzcf bire gur 7 ynml qbtf"),
                         "The quick brown fox jumps over the 2 lazy dogs")
