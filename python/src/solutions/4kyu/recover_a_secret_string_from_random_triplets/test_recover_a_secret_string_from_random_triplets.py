"""https://www.codewars.com/kata/53f40dff5f9d31b813000774"""
import pytest

from solution_recover_a_secret_string_from_random_triplets import *


@pytest.mark.parametrize('triplets, secret', [
    ([
         ['t', 'u', 'p'],
         ['w', 'h', 'i'],
         ['t', 's', 'u'],
         ['a', 't', 's'],
         ['h', 'a', 'p'],
         ['t', 'i', 's'],
         ['w', 'h', 's']
     ], 'whatisup'),
    ([
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
     ], 'mathisfun'),
    ([
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
     ], 'congrats')
])
def test_example(triplets, secret):
    assert recover_secret(triplets) == secret
