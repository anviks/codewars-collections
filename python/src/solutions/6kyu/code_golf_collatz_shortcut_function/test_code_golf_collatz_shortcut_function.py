"""https://www.codewars.com/kata/664bb069388167b5923b1688"""

import inspect

from solution_code_golf_collatz_shortcut_function import g


def test_code_length_test():
    source = inspect.getsource(g)
    length = len(source)
    max_length = 26
    error_message = f'Your code is too long: {length} should be no more than {max_length}.'
    assert length <= max_length, error_message


def test_fixed_tests__testing_simple_numbers():
    assert g(5) == 8, 'Tiny odd input'
    assert g(10) == 5, 'Tiny even input'
    assert g(15) == 23, 'Another tiny odd input'
    assert g(1515) == 2273.0, 'This may or may not be a hint'
