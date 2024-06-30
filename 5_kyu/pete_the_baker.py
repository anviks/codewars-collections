"""https://www.codewars.com/kata/525c65e51bf619685c000059"""
from collections import defaultdict
import sys


def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
    possible = sys.maxsize
    available = defaultdict(int, available)
    
    for k, v in recipe.items():
        possible = min(possible, available[k] // v)
    
    return possible


def main():
    recipe = {"flour": 500, "sugar": 200, "eggs": 1}
    available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
    print(cakes(recipe, available), 2)

    recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
    available = {"sugar": 500, "flour": 2000, "milk": 2000}
    print(cakes(recipe, available), 0)


if __name__ == '__main__':
    main()

