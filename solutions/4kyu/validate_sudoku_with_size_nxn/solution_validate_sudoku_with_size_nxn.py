"""https://www.codewars.com/kata/540afbe2dc9f615d5e000425"""


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
