"""https://www.codewars.com/kata/5503013e34137eeeaa001648"""

from solution_give_me_a_diamond import *


def test_fixed_tests__basic_test_cases():
    expected = ' *\n'
    expected += '***\n'
    expected += ' *\n'
    assert diamond(1) == '*\n'
    assert diamond(2) is None
    assert diamond(3) == expected
    assert diamond(5) == '  *\n ***\n*****\n ***\n  *\n'
    assert diamond(0) is None
    assert diamond(-3) is None
