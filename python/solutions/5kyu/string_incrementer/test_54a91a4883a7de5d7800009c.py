"""https://www.codewars.com/kata/54a91a4883a7de5d7800009c"""

import unittest

from solution import increment_string


class BasicTests(unittest.TestCase):
    def test_basic_tests(self):
        self.assertEqual(increment_string("foo"), "foo1")
        self.assertEqual(increment_string("foobar001"), "foobar002")
        self.assertEqual(increment_string("foobar1"), "foobar2")
        self.assertEqual(increment_string("foobar00"), "foobar01")
        self.assertEqual(increment_string("foobar99"), "foobar100")
        self.assertEqual(increment_string("foobar099"), "foobar100")
        self.assertEqual(increment_string("fo99obar99"), "fo99obar100")
        self.assertEqual(increment_string(""), "1")
