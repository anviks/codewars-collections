"""
https://www.codewars.com/kata/5296bc77afba8baa690002d7

**Sudoku Solver**

Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument consisting of the 2D puzzle
array, with the value `0` representing an unknown square.

The Sudokus tested against your function will be "easy" (i.e. determinable; there will be no need to assume and test
possibilities on unknowns) and can be solved with a brute-force approach.

For Sudoku rules, see the Wikipedia article.
"""


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    zero_count = 0

    for row in puzzle:
        for col in row:
            if col == 0:
                zero_count += 1

    while zero_count > 0:
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    possible_values = (set(range(10))
                                       - get_row_values(puzzle, i)
                                       - get_column_values(puzzle, j)
                                       - get_square_values(puzzle, i, j))

                    if len(possible_values) == 1:
                        puzzle[i][j] = possible_values.pop()
                        zero_count -= 1

    return puzzle


def get_row_values(puzzle, row_index):
    return set(puzzle[row_index])


def get_column_values(puzzle, column_index):
    return {puzzle[i][column_index] for i in range(9)}


def get_square_values(puzzle, row_index, column_index):
    return {puzzle[row_index // 3 * 3 + j // 3][column_index // 3 * 3 + j % 3] for j in range(9)}


def is_solved(puzzle):
    for row in puzzle:
        if len(set(row)) < 9 or 0 in row:
            return False

    for j in range(9):
        col_values = {puzzle[i][j] for i in range(9)}
        if len(col_values) < 9 or 0 in col_values:
            return False

    for i in range(9):
        square_values = {puzzle[i // 3 * 3 + j // 3][i % 3 * 3 + j % 3] for j in range(9)}

        if len(square_values) < 9 or 0 in square_values:
            return False

    return True


if __name__ == '__main__':
    puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    print(get_square_values(puzzle, 5, 4))

    solution = sudoku(puzzle)
    print(solution)

    print(is_solved(puzzle))

    expected_solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                         [6, 7, 2, 1, 9, 5, 3, 4, 8],
                         [1, 9, 8, 3, 4, 2, 5, 6, 7],
                         [8, 5, 9, 7, 6, 1, 4, 2, 3],
                         [4, 2, 6, 8, 5, 3, 7, 9, 1],
                         [7, 1, 3, 9, 2, 4, 8, 5, 6],
                         [9, 6, 1, 5, 3, 7, 2, 8, 4],
                         [2, 8, 7, 4, 1, 9, 6, 3, 5],
                         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    assert solution == expected_solution
