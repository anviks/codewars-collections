"""https://www.codewars.com/kata/multi-line-task-hello-world-easy-one"""

import unittest

from solution import f


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(f(), 'Hello, world!')
