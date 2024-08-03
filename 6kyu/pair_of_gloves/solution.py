"""https://www.codewars.com/kata/58235a167a8cb37e1a0000db"""

from collections import Counter


def number_of_pairs(gloves: list[str]):
    return sum(n // 2 for n in Counter(gloves).values())
