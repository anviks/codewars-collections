"""https://www.codewars.com/kata/53855e4dc25c8adbc5000316"""

from solution_email_validation_1 import *


def test_example():
    assert validate('abc@example.com') is True
    assert validate('_bc@example.com') is False
