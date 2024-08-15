"""https://www.codewars.com/kata/559a28007caad2ac4e000083"""

import unittest

from solution_559a28007caad2ac4e000083 import perimeter


class Testing(unittest.TestCase):
    def test_fixed_tests(self):
        self.assertEqual(perimeter(5), 80)
        self.assertEqual(perimeter(7), 216)
        self.assertEqual(perimeter(20), 114624)
        self.assertEqual(perimeter(30), 14098308)
        self.assertEqual(perimeter(100), 6002082144827584333104)
        self.assertEqual(perimeter(500),
                         2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)
