"""https://www.codewars.com/kata/5588bd9f28dbb06f43000085"""


class Sudoku:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.size = len(puzzle)
        self.box_size = int(self.size ** 0.5)

    def is_valid(self, row, col, num):
        for i in range(self.size):
            if self.puzzle[row][i] == num or self.puzzle[i][col] == num:
                return False

        start_row = row - row % self.box_size
        start_col = col - col % self.box_size

        for i in range(self.box_size):
            for j in range(self.box_size):
                if self.puzzle[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.puzzle[row][col] == 0:
                    for num in range(1, self.size + 1):
                        if self.is_valid(row, col, num):
                            self.puzzle[row][col] = num
                            if self.solve():
                                return True
                            self.puzzle[row][col] = 0
                    return False
        return True

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.puzzle)


def sudoku_solver(puzzle):
    sudoku = Sudoku(puzzle)
    sudoku.solve()
    return sudoku.puzzle
