"""https://www.codewars.com/kata/55f8a9c06c018a0d6e000132"""

from solution_regex_validate_pin_code import *


def test_fixed_tests__should_return_false_for_pins_with_length_other_than_4_or_6():
    assert validate_pin('1') is False, "Wrong output for '1'"
    assert validate_pin('12') is False, "Wrong output for '12'"
    assert validate_pin('123') is False, "Wrong output for '123'"
    assert validate_pin('12345') is False, "Wrong output for '12345'"
    assert validate_pin('1234567') is False, "Wrong output for '1234567'"
    assert validate_pin('-1234') is False, "Wrong output for '-1234'"
    assert validate_pin('-12345') is False, "Wrong output for '-12345'"
    assert validate_pin('1.234') is False, "Wrong output for '1.234'"
    assert validate_pin('00000000') is False, "Wrong output for '00000000'"


def test_fixed_tests__should_return_false_for_pins_which_contain_characters_other_than_digits():
    assert validate_pin('a234') is False, "Wrong output for 'a234'"
    assert validate_pin('.234') is False, "Wrong output for '.234'"


def test_fixed_tests__should_return_true_for_valid_pins():
    assert validate_pin('1234') is True, "Wrong output for '1234'"
    assert validate_pin('0000') is True, "Wrong output for '0000'"
    assert validate_pin('1111') is True, "Wrong output for '1111'"
    assert validate_pin('123456') is True, "Wrong output for '123456'"
    assert validate_pin('098765') is True, "Wrong output for '098765'"
    assert validate_pin('000000') is True, "Wrong output for '000000'"
    assert validate_pin('123456') is True, "Wrong output for '123456'"
    assert validate_pin('090909') is True, "Wrong output for '090909'"
