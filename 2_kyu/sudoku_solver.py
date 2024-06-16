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


def main():
    puzzle = [
        [0, 0, 6, 1, 0, 0, 0, 0, 8],
        [0, 8, 0, 0, 9, 0, 0, 3, 0],
        [2, 0, 0, 0, 0, 5, 4, 0, 0],
        [4, 0, 0, 0, 0, 1, 8, 0, 0],
        [0, 3, 0, 0, 7, 0, 0, 4, 0],
        [0, 0, 7, 9, 0, 0, 0, 0, 3],
        [0, 0, 8, 4, 0, 0, 0, 0, 6],
        [0, 2, 0, 0, 5, 0, 0, 8, 0],
        [1, 0, 0, 0, 0, 2, 5, 0, 0]
    ]

    solution = [
        [3, 4, 6, 1, 2, 7, 9, 5, 8],
        [7, 8, 5, 6, 9, 4, 1, 3, 2],
        [2, 1, 9, 3, 8, 5, 4, 6, 7],
        [4, 6, 2, 5, 3, 1, 8, 7, 9],
        [9, 3, 1, 2, 7, 8, 6, 4, 5],
        [8, 5, 7, 9, 4, 6, 2, 1, 3],
        [5, 9, 8, 4, 1, 3, 7, 2, 6],
        [6, 2, 4, 7, 5, 9, 3, 8, 1],
        [1, 7, 3, 8, 6, 2, 5, 9, 4]
    ]
    
    assert sudoku_solver(puzzle) == solution


if __name__ == '__main__':
    main()
