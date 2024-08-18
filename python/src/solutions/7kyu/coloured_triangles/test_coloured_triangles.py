"""https://www.codewars.com/kata/5a25ac6ac5e284cfbe000111"""

from solution_coloured_triangles import triangle


def test_fixed_tests__basic_test_cases():
    assert triangle('GB') == 'R'
    assert triangle('RRR') == 'R'
    assert triangle('RGBG') == 'B'
    assert triangle('RBRGBRB') == 'G'
    assert triangle('RBRGBRBGGRRRBGBBBGG') == 'G'
    assert triangle('B') == 'B'
