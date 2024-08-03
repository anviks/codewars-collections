"""https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2"""

import unittest

from solution import validate


class SampleTests(unittest.TestCase):
    def test_some_examples(self):
        self.assertEqual(validate(1714), False)
        self.assertEqual(validate(12345), False)
        self.assertEqual(validate(891), False)
        self.assertEqual(validate(123), False)
        self.assertEqual(validate(1), False)
        self.assertEqual(validate(2121), True)
        self.assertEqual(validate(1230), True)
