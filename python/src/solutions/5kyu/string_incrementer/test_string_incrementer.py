"""https://www.codewars.com/kata/54a91a4883a7de5d7800009c"""

from solution_string_incrementer import *


def test_basic_tests__basic_tests():
    assert increment_string('foo') == 'foo1'
    assert increment_string('foobar001') == 'foobar002'
    assert increment_string('foobar1') == 'foobar2'
    assert increment_string('foobar00') == 'foobar01'
    assert increment_string('foobar99') == 'foobar100'
    assert increment_string('foobar099') == 'foobar100'
    assert increment_string('fo99obar99') == 'fo99obar100'
    assert increment_string('') == '1'
