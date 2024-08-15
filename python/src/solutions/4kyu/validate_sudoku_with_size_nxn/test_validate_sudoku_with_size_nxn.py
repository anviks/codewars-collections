"""https://www.codewars.com/kata/540afbe2dc9f615d5e000425"""

import unittest

from solution_validate_sudoku_with_size_nxn import Sudoku


class ValidateSudoku(unittest.TestCase):
    # @formatter:off
    # Valid Sudoku
    good_sudoku1 = Sudoku([
        [7, 8, 4,   1, 5, 9,   3, 2, 6],
        [5, 3, 9,   6, 7, 2,   8, 4, 1],
        [6, 1, 2,   4, 3, 8,   7, 5, 9],
  
        [9, 2, 8,   7, 1, 5,   4, 6, 3],
        [3, 5, 7,   8, 4, 6,   1, 9, 2],
        [4, 6, 1,   9, 2, 3,   5, 8, 7],
  
        [8, 7, 6,   3, 9, 4,   2, 1, 5],
        [2, 4, 3,   5, 6, 1,   9, 7, 8],
        [1, 9, 5,   2, 8, 7,   6, 3, 4]
    ])

    good_sudoku2 = Sudoku([
        [1, 4,   2, 3],
        [3, 2,   4, 1],

        [4, 1,   3, 2],
        [2, 3,   1, 4]
    ])

    # Invalid Sudoku
    bad_sudoku1 = Sudoku([
        [0, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9],

        [1, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9],

        [1, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9],
        [1, 2, 3,   4, 5, 6,   7, 8, 9]
    ])

    bad_sudoku2 = Sudoku([
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1]
    ])
    # @formatter:on

    def test_should_be_valid(self):
        self.assertTrue(self.good_sudoku1.is_valid(), 'Testing valid 9x9')
        self.assertTrue(self.good_sudoku2.is_valid(), 'Testing valid 4x4')

    def test_should_be_invalid(self):
        self.assertFalse(self.bad_sudoku1.is_valid(), 'Values in wrong order')
        self.assertFalse(self.bad_sudoku2.is_valid(), '4x5 (invalid dimension)')
