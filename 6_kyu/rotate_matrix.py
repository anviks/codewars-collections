"""https://www.codewars.com/kata/5919f3bf6589022915000023"""


def rotate_against_clockwise(matrix, times):
    for _ in range(times % 4):
        matrix = list(zip(*matrix))[::-1]
    return [list(row) for row in matrix]


def main():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]

    times_to_turn = 1

    print(rotate_against_clockwise(matrix, times_to_turn))


if __name__ == '__main__':
    main()
