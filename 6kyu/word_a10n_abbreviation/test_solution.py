"""https://www.codewars.com/kata/5375f921003bf62192000746"""

import unittest

from solution import abbreviate


class SampleTests(unittest.TestCase):
    def test_tests(self):
        self.assertEqual(abbreviate("internationalization"), "i18n")
        self.assertEqual(abbreviate("accessibility"), "a11y")
        self.assertEqual(abbreviate("Accessibility"), "A11y")
        self.assertEqual(abbreviate("elephant-ride"), "e6t-r2e")
