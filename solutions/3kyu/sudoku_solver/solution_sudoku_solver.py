"""https://www.codewars.com/kata/5296bc77afba8baa690002d7"""


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
