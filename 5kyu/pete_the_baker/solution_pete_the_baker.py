"""https://www.codewars.com/kata/525c65e51bf619685c000059"""

import sys
from collections import defaultdict


def cakes(recipe: dict[str, int], available: dict[str, int]) -> int:
    possible = sys.maxsize
    available = defaultdict(int, available)

    for k, v in recipe.items():
        possible = min(possible, available[k] // v)

    return possible
