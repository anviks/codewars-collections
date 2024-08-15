"""https://www.codewars.com/kata/55f8a9c06c018a0d6e000132"""

import unittest

from solution import validate_pin


class FixedTests(unittest.TestCase):
    def test_should_return_false_for_pins_with_length_other_than_4_or_6(self):
        self.assertEqual(validate_pin("1"), False, "Wrong output for '1'")
        self.assertEqual(validate_pin("12"), False, "Wrong output for '12'")
        self.assertEqual(validate_pin("123"), False, "Wrong output for '123'")
        self.assertEqual(validate_pin("12345"), False, "Wrong output for '12345'")
        self.assertEqual(validate_pin("1234567"), False, "Wrong output for '1234567'")
        self.assertEqual(validate_pin("-1234"), False, "Wrong output for '-1234'")
        self.assertEqual(validate_pin("-12345"), False, "Wrong output for '-12345'")
        self.assertEqual(validate_pin("1.234"), False, "Wrong output for '1.234'")
        self.assertEqual(validate_pin("00000000"), False, "Wrong output for '00000000'")

    def test_should_return_false_for_pins_which_contain_characters_other_than_digits(self):
        self.assertEqual(validate_pin("a234"), False, "Wrong output for 'a234'")
        self.assertEqual(validate_pin(".234"), False, "Wrong output for '.234'")

    def test_should_return_true_for_valid_pins(self):
        self.assertEqual(validate_pin("1234"), True, "Wrong output for '1234'")
        self.assertEqual(validate_pin("0000"), True, "Wrong output for '0000'")
        self.assertEqual(validate_pin("1111"), True, "Wrong output for '1111'")
        self.assertEqual(validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(validate_pin("098765"), True, "Wrong output for '098765'")
        self.assertEqual(validate_pin("000000"), True, "Wrong output for '000000'")
        self.assertEqual(validate_pin("123456"), True, "Wrong output for '123456'")
        self.assertEqual(validate_pin("090909"), True, "Wrong output for '090909'")
