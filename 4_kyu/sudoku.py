"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""


class Sudoku(object):
    def __init__(self, data: list[list[int]]):
        self.data = data
        self.size = len(data)
        self.sub_size = int(self.size ** 0.5)
        self.valid_nums = set(range(1, self.size + 1))

    def is_valid(self) -> bool:
        if not self.data or not self.data[0]:
            return False
        equal_rows = len({len(row) for row in self.data}) == 1
        is_square = len(self.data) == len(self.data[0])
        if not all((equal_rows, is_square)):
            return False

        return all((self.__check_rows(), self.__check_columns(), self.__check_squares())) \
            and "True" not in [str(i) for j in self.data for i in j]

    def __check_rows(self) -> bool:
        for row in self.data:
            if set(row) != self.valid_nums:
                return False
        return True

    def __check_columns(self) -> bool:
        for i in range(len(self.data)):
            column = [row[i] for row in self.data]
            if set(column) != self.valid_nums:
                return False
        return True

    def __check_squares(self) -> bool:
        for i in range(0, self.size, self.sub_size):
            for j in range(0, self.size, self.sub_size):
                square = []
                for k in range(self.sub_size):
                    square += self.data[i + k][j:j + self.sub_size]
                if set(square) != self.valid_nums:
                    return False
        return True


if __name__ == '__main__':
    sudoku = Sudoku([
        [1, 2, 3,   4, 5, 6,    7, 8, 9],
        [2, 3, 1,   5, 6, 4,    8, 9, 7],
        [3, 1, 2,   6, 4, 5,    9, 7, 8],

        [4, 5, 6,   7, 8, 9,    1, 2, 3],
        [5, 6, 4,   8, 9, 7,    2, 3, 1],
        [6, 4, 5,   9, 7, 8,    3, 1, 2],

        [7, 8, 9,   1, 2, 3,    4, 5, 6],
        [8, 9, 7,   2, 3, 1,    5, 6, 4],
        [9, 7, 8,   3, 1, 2,    6, 4, 5]
    ])

    print(sudoku.is_valid())
    print(Sudoku([[True]]).is_valid())
