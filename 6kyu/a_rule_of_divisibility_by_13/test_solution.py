"""https://www.codewars.com/kata/564057bc348c7200bd0000ff"""

import unittest

from solution import thirt


class Thirt(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(thirt(8529), 79)
        self.assertEqual(thirt(85299258), 31)
        self.assertEqual(thirt(5634), 57)
        self.assertEqual(thirt(1111111111), 71)
        self.assertEqual(thirt(987654321), 30)
