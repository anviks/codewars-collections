"""https://www.codewars.com/kata/57814d79a56c88e3e0000786"""

from solution_simple_encryption_number_1_alternating_split import *


def test_fixed_tests__encrypt():
    assert encrypt('This is a test!', 0) == 'This is a test!'
    assert encrypt('This is a test!', 1) == 'hsi  etTi sats!'
    assert encrypt('This is a test!', 2) == 's eT ashi tist!'
    assert encrypt('This is a test!', 3) == ' Tah itse sits!'
    assert encrypt('This is a test!', 4) == 'This is a test!'
    assert encrypt('This is a test!', -1) == 'This is a test!'
    assert encrypt('This kata is very interesting!', 1) == 'hskt svr neetn!Ti aai eyitrsig'


def test_fixed_tests__decrypt():
    assert decrypt('This is a test!', 0) == 'This is a test!'
    assert decrypt('hsi  etTi sats!', 1) == 'This is a test!'
    assert decrypt('s eT ashi tist!', 2) == 'This is a test!'
    assert decrypt(' Tah itse sits!', 3) == 'This is a test!'
    assert decrypt('This is a test!', 4) == 'This is a test!'
    assert decrypt('This is a test!', -1) == 'This is a test!'
    assert decrypt('hskt svr neetn!Ti aai eyitrsig', 1) == 'This kata is very interesting!'


def test_fixed_tests__empty_strings_and_invalid_cases():
    assert encrypt('', 0) == ''
    assert decrypt('', 0) == ''
    assert encrypt(None, 0) is None
    assert decrypt(None, 0) is None
