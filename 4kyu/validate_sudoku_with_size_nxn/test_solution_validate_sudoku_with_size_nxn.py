"""https://www.codewars.com/kata/540afbe2dc9f615d5e000425"""


from solution import Sudoku
import unittest

class ValidateSudoku(unittest.TestCase):
    
    # Valid Sudoku
    goodSudoku1 = Sudoku([
      [7,8,4, 1,5,9, 3,2,6],
      [5,3,9, 6,7,2, 8,4,1],
      [6,1,2, 4,3,8, 7,5,9],
    
      [9,2,8, 7,1,5, 4,6,3],
      [3,5,7, 8,4,6, 1,9,2],
      [4,6,1, 9,2,3, 5,8,7],
      
      [8,7,6, 3,9,4, 2,1,5],
      [2,4,3, 5,6,1, 9,7,8],
      [1,9,5, 2,8,7, 6,3,4]
    ])
    
    goodSudoku2 = Sudoku([
      [1,4, 2,3],
      [3,2, 4,1],
    
      [4,1, 3,2],
      [2,3, 1,4]
    ])
    
    # Invalid Sudoku
    badSudoku1 = Sudoku([
      [0,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9],
      [1,2,3, 4,5,6, 7,8,9]
    ])
    
    badSudoku2 = Sudoku([
      [1,2,3,4,5],
      [1,2,3,4],
      [1,2,3,4],  
      [1]
    ])
    
    def test_should_be_valid(self):
        self.assertEqual(goodSudoku1.is_valid(), True, 'Testing valid 9x9')
        self.assertEqual(goodSudoku2.is_valid(), True, 'Testing valid 4x4')
    
    @test.it ('should be invalid')
    def should_be_invalid(self):
        self.assertEqual(badSudoku1.is_valid(), False, 'Values in wrong order')
        self.assertEqual(badSudoku2.is_valid(), False, '4x5 (invalid dimension)')
