"""https://www.codewars.com/kata/simple-encryption-number-2-index-difference"""

import pytest

from solution_simple_encryption_number_2_index_difference import *


def test_basic_encrypt_tests():
    assert encrypt('Business') == '&61kujla'
    assert encrypt(
        'Do the kata "Kobayashi-Maru-Test!" Endless fun and excitement when finding a solution!') == "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w"
    assert encrypt('This is a test!') == '5MyQa9p0riYplZc'
    assert encrypt('This kata is very interesting!') == "5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p"


def test_basic_decrypt_tests():
    assert decrypt(
        "$-Wy,dM79H'i'o$n0C&I.ZTcMJw5vPlZc Hn!krhlaa:khV mkL;gvtP-S7Rt1Vp2RV:wV9VuhO Iz3dqb.U0w") == 'Do the kata "Kobayashi-Maru-Test!" Endless fun and excitement when finding a solution!'
    assert decrypt('5MyQa9p0riYplZc') == 'This is a test!'
    assert decrypt("5MyQa79H'ijQaw!Ns6jVtpmnlZ.V6p") == 'This kata is very interesting!'


def test_none_or_empty():
    assert encrypt('') == ''
    assert decrypt('') == ''
    assert encrypt(None) is None
    assert decrypt(None) is None


def test_not_allowed_chars():
    with pytest.raises(ValueError):
        encrypt("A5#")
    with pytest.raises(ValueError):
        decrypt("A5#")
