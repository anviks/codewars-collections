"""https://www.codewars.com/kata/59c633e7dcc4053512000073"""

from solution_consonant_value import *


def test_fixed_tests__basic_test_cases():
    assert solve('cozy') == 51
    assert solve('xyzzy') == 126
    assert solve('zodiac') == 26
    assert solve('chruschtschov') == 80
    assert solve('khrushchev') == 38
    assert solve('strength') == 57
    assert solve('catchphrase') == 73
    assert solve('twelfthstreet') == 103
    assert solve('mischtschenkoana') == 80
