"""https://www.codewars.com/kata/5919f3bf6589022915000023"""


def rotate_against_clockwise(matrix, times):
    for _ in range(times % 4):
        matrix = list(zip(*matrix))[::-1]
    return [list(row) for row in matrix]
