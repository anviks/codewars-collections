"""https://www.codewars.com/kata/56a921fa8c5167d8e7000053"""

from solution_password_validator import *


def test_basic_tests():
    assert password('Abcd1234') is True
    assert password('Abcd123') is False
    assert password('abcd1234') is False
    assert password('AbcdefGhijKlmnopQRsTuvwxyZ1234567890') is True
    assert password('ABCD1234') is False
    assert password('Ab1!@#$%^&*()-_+={}[]|\\:;?/>.<,') is True
    assert password('!@#$%^&*()-_+={}[]|\\:;?/>.<,') is False
    assert password('') is False
    assert password(' aA1----') is True
    assert password('4aA1----') is True
