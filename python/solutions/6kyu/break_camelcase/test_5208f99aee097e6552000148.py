"""https://www.codewars.com/kata/5208f99aee097e6552000148"""

import unittest

from solution_5208f99aee097e6552000148 import *


class FixedTests(unittest.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(solution("helloWorld"), "hello World")
        self.assertEqual(solution("camelCase"), "camel Case")
        self.assertEqual(solution("breakCamelCase"), "break Camel Case")
