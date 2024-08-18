"""https://www.codewars.com/kata/5208f99aee097e6552000148"""

from solution_break_camelcase import *


def test_fixed_tests__basic_test_cases():
    assert solution('helloWorld') == 'hello World'
    assert solution('camelCase') == 'camel Case'
    assert solution('breakCamelCase') == 'break Camel Case'
