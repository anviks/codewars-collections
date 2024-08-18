"""https://www.codewars.com/kata/5202ef17a402dd033c000009"""

from solution_title_case import *


def test_sample_tests__tests():
    assert title_case('') == ''
    assert title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings'
    assert title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows'
    assert title_case('the quick brown fox') == 'The Quick Brown Fox'
