"""https://www.codewars.com/kata/5a331ea7ee1aae8f24000175"""

import pytest

from solution_insane_coloured_triangles import triangle


@pytest.mark.parametrize('_in, _out', [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G'],
    ['BBRGBRBGGGRG', 'G'],
    
    ['BBRGBRBGGGG', 'R'],
    ['BBRGBRBGGG', 'R'],
])
def test_basic_cases(_in, _out):
    assert triangle(_in) == _out


@pytest.mark.parametrize('_in, _out', [
    [
        'GRRBRRGGGGGGBBGBRRGRRGBGGRBBGBBGBRRBGBBGGBRRRRRGBBBBRRGBRBBBBBGGRBGBBRRRGRRBBGGBRBRGBRGRGGGGGRRBRG',
        'G'
    ],
    [
        'BRRBRRGGGGGGBBGBRRGRRGBGGRBBGBBGBRRBGBBGGBRRRRRGBBBBRRGBRBBBBBGGRBGBBRRRGRRBBGGBRBRGBRGRGGGGGRRBRGGBRBRBBGGGRBGRRBRBBRRBRBGBGBRRGGBRGRGBGRGBBBRRGBRRGGGRRBRRBRGRBRBBGBGGGBGRBRGRBGRBGRRRBRGRBGBGRRBBRGBRBRRGRRGGGGBGBBGRRGBGGGRBBGGBBBGRRBBGRBRBBRBRGGGBRRGRGRRRGBGBBRGRGBGGGBBRRRGRRBRBGGBBRGB',
        'G'
    ],
    [
        'RRGRRRRGRGBRRRBBRGGBRBRGRBBBGBRGRBRBBBGBRRGRRGBGRBGBGBRRRRGRBGBBGBBGBRRBRRGBRRGBBGGRGGRRBBRRRRRGRRBBBBBRGRGRGBBGGBBGRGRRGRGBGBGRBBBGGRGGBGRBBRBGGBGRBRBRRGRRRGRRGGRRGRRGBGBRBRBGBRRGGRRBBGBGBBBRGGRRRBRBRBGGRGBRBGRRRRRRRBGBGBGRGBRGGGBGRGGRGGRGRBRRGBGGGRGRRRBBBRRBGRBBRRGRBBGRGBRGRGGRRRGRRGGBGBBGBGBGRGGBBBGRBBGRBRGGBGRBBGBGBBGGGRBGGGRGGGRGBGRGBBBBRGRRRRGRGRBRBGBRRBGBGRBGGRGRRRBRRGRBBGBGGBBRBBGRGBBGBGRGRRRBRRRRBBRGGGBRBGGBBRBGGRRGGRBGRBRGBGRRGRRBBBGBBBGRBRRBRBBGBRBBBRRGGGBBBRRGRRBRRRBRGRGGRBBRGBGRRBRBRGGBGRBGBBBGGGRGBRBRGGRBRRRGRRGBBGBBRRGGGGGRBGRGRBRGGGBBRBRBGGRBGRGBRRRGGGBBBGGGBGGBRRBBGRGBBRGBGBGGBGGBRRGGGGBRRBGBGRBGBRBRGRBRBBGRGBRRBBBRGGBRBGBBGBBGBBBRBBGGGBGRGBBBRRBBBRBBGRBGBRGBRRBRGBBBBBBBGGBBRGRBBRBRGRGGRGBBBRBGBRGRG',
        'G'
    ],
    [
        'RRGRRRRGRGBRRRBBRGGBRRGRBBBGBRGRBRBBBGBRRGRRGBGRBGBGBRRRRGRBGBBGBBGBRRBRRGBRRGBBGGRGGRRBBRRRRRGRRBBBBBRGRGRGBBGGBBGRGRRGRGBGBGRBBBGGRGGBGRBBRBGGBGRBRBRRGRRRGRRGGRRGRRGBGBRBRBGBRRGGRRBBGBGBBBRGGRRRBRBRBGGRGBRBGRRRRRRRBGBGBGRGBRGGGBGRGGRGGRGRBRRGBGGGRGRRRBBBRRBGRBBRRGRBBGRGBRGRGGRRRGRRGGBGBBGBGBGRGGBBBGRBBGRBRGGBGRBBGBGBBGGGRBGGGRGGGRGBGRGBBBBRGRRRRGRGRBRBGBRRBGBGRBGGRGRRRBRRGRBBGBGGBBRBBGRGBBGBGRGRRRBRRRRBBRGGGBRBGGBBRBGGRRGGRBGRBRGBGRRGRRBBBGBBBGRBRRBRBBGBRBBBRRGGGBBBRRGRRBRRRBRGRGGRBBRGBGRRBRBRGGBGRBGBBBGGGRGBRBRGGRBRRRGRRGBBGBBRRGGGGGRBGRGRBRGGGBBRBRBGGRBGRGBRRRGGGBBBGGGBGGBRRBBGRGBBRGBGBGGBGGBRRGGGGBRRBGBGRBGBRBRGRBRBBGRGBRRBBBRGGBRBGBBGBBGBBBRBBGGGBGRGBBBRRBBBRBBGRBGBRGBRRBRGBBBBBBBGGBBRGRBBRBRGRGGRGBBBRBGBRGRG',
        'B'
    ],
])
def test_advanced_cases(_in, _out):
    assert triangle(_in) == _out
