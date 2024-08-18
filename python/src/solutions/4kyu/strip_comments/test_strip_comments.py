"""https://www.codewars.com/kata/strip-comments"""

from solution_strip_comments import *


def test_test_case__example():
    assert strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples',
                          ['#', '!']) == 'apples, pears\ngrapes\nbananas'
    assert strip_comments('a #b\nc\nd $e f g', ['#', '$']) == 'a\nc\nd'
    assert strip_comments(' a #b\nc\nd $e f g', ['#', '$']) == ' a\nc\nd'
