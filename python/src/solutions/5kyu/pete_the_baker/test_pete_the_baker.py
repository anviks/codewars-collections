"""https://www.codewars.com/kata/525c65e51bf619685c000059"""

from solution_pete_the_baker import *


def test_testing_pete_the_baker():
    recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
    available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
    assert cakes(recipe, available) == 2, 'example #1'

    recipe = {'apples': 3, 'flour': 300, 'sugar': 150, 'milk': 100, 'oil': 100}
    available = {'sugar': 500, 'flour': 2000, 'milk': 2000}
    assert cakes(recipe, available) == 0, 'example #2'
