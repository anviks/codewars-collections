"""https://www.codewars.com/kata/525f47c79f2f25a4db000025"""

import unittest

from solution_525f47c79f2f25a4db000025 import valid_phone_number


class PhoneNumberValidations(unittest.TestCase):
    def test_sample_tests(self):
        self.assertEqual(valid_phone_number("(123) 456-7890"), True)
        self.assertEqual(valid_phone_number("(1111)555 2345"), False)
        self.assertEqual(valid_phone_number("(098) 123 4567"), False)
        self.assertEqual(valid_phone_number("(123)456-7890"), False)
        self.assertEqual(valid_phone_number("abc(123)456-7890"), False)
        self.assertEqual(valid_phone_number("(123)456-7890abc"), False)
        self.assertEqual(valid_phone_number("abc(123)456-7890abc"), False)
        self.assertEqual(valid_phone_number("abc(123) 456-7890"), False)
        self.assertEqual(valid_phone_number("(123) 456-7890abc"), False)
        self.assertEqual(valid_phone_number("abc(123) 456-7890abc"), False)
        self.assertEqual(valid_phone_number("(333) 185-0594"), True)
