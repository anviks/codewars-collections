"""https://www.codewars.com/kata/53f40dff5f9d31b813000774"""
import unittest

from parameterized import parameterized

from solution_53f40dff5f9d31b813000774 import recover_secret


class SolutionTests(unittest.TestCase):
    @parameterized.expand([
        ('whatisup', [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]),
        ('mathisfun', [
            ['t', 's', 'f'],
            ['a', 's', 'u'],
            ['m', 'a', 'f'],
            ['a', 'i', 'n'],
            ['s', 'u', 'n'],
            ['m', 'f', 'u'],
            ['a', 't', 'h'],
            ['t', 'h', 'i'],
            ['h', 'i', 'f'],
            ['m', 'h', 'f'],
            ['a', 'u', 'n'],
            ['m', 'a', 't'],
            ['f', 'u', 'n'],
            ['h', 's', 'n'],
            ['a', 'i', 's'],
            ['m', 's', 'n'],
            ['m', 's', 'u']
        ]),
        ('congrats', [
            ['g', 'a', 's'],
            ['o', 'g', 's'],
            ['c', 'n', 't'],
            ['c', 'o', 'n'],
            ['a', 't', 's'],
            ['g', 'r', 't'],
            ['r', 't', 's'],
            ['c', 'r', 'a'],
            ['g', 'a', 't'],
            ['n', 'g', 's'],
            ['o', 'a', 's']
        ])
    ])
    def test_solution(self, secret, triplets):
        self.assertEqual(secret, recover_secret(triplets))
