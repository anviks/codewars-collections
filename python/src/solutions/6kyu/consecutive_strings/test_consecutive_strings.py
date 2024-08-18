"""https://www.codewars.com/kata/56a5d994ac971f1ac500003e"""

from solution_consecutive_strings import *


def test_fixed_tests__basic_test_cases():
    assert longest_consec(['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], 2) == 'abigailtheta'
    assert longest_consec(['ejjjjmmtthh', 'zxxuueeg', 'aanlljrrrxx', 'dqqqaaabbb', 'oocccffuucccjjjkkkjyyyeehh'],
                          1) == 'oocccffuucccjjjkkkjyyyeehh'
    assert longest_consec([], 3) == ''
    assert longest_consec(['itvayloxrp', 'wkppqsztdkmvcuwvereiupccauycnjutlv', 'vweqilsfytihvrzlaodfixoyxvyuyvgpck'],
                          2) == 'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck'
    assert longest_consec(['wlwsasphmxx', 'owiaxujylentrklctozmymu', 'wpgozvxxiu'],
                          2) == 'wlwsasphmxxowiaxujylentrklctozmymu'
    assert longest_consec(['zone', 'abigail', 'theta', 'form', 'libe', 'zas'], -2) == ''
    assert longest_consec(['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 3) == 'ixoyx3452zzzzzzzzzzzz'
    assert longest_consec(['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 15) == ''
    assert longest_consec(['it', 'wkppv', 'ixoyx', '3452', 'zzzzzzzzzzzz'], 0) == ''
