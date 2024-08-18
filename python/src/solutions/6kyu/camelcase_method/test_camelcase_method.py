"""https://www.codewars.com/kata/587731fda577b3d1b0001196"""

from solution_camelcase_method import *


def test_basic_tests__basic_tests():
    assert camel_case('test case') == 'TestCase'
    assert camel_case('camel case method') == 'CamelCaseMethod'
    assert camel_case('say hello ') == 'SayHello'
    assert camel_case(' camel case word') == 'CamelCaseWord'
    assert camel_case('') == ''
