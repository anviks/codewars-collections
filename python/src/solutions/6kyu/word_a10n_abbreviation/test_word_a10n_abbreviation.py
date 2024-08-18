"""https://www.codewars.com/kata/5375f921003bf62192000746"""

from solution_word_a10n_abbreviation import *


def test_sample_tests__tests():
    assert abbreviate('internationalization') == 'i18n'
    assert abbreviate('accessibility') == 'a11y'
    assert abbreviate('Accessibility') == 'A11y'
    assert abbreviate('elephant-ride') == 'e6t-r2e'
