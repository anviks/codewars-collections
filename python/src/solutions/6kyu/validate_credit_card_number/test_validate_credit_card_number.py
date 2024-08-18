"""https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2"""

from solution_validate_credit_card_number import *


def test_sample_tests__some_examples():
    assert validate(1714) is False
    assert validate(12345) is False
    assert validate(891) is False
    assert validate(123) is False
    assert validate(1) is False
    assert validate(2121) is True
    assert validate(1230) is True
