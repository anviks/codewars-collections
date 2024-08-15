"""https://www.codewars.com/kata/one-line-task-squirrel-and-tree"""
import unittest

from solution_one_line_task_squirrel_and_tree import squirrel


class Tests(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(squirrel(4, 16, 3), 20)
        self.assertEqual(squirrel(4, 4, 3), 5)
        self.assertEqual(squirrel(8, 9, 37), 42.5869)
        self.assertEqual(squirrel(526, 682, 140), 705.7435)
        self.assertEqual(squirrel(247, 857, 669), 2474.3392)
        self.assertEqual(squirrel(2, 11, 47), 258.7339)
        self.assertEqual(squirrel(73, 97, 244), 338.4185)
        self.assertEqual(squirrel(15, 774, 948), 48922.923)
        self.assertEqual(squirrel(21, 29, 60), 87.7856)
        self.assertEqual(squirrel(83, 97, 86), 139.6799)
