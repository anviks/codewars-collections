"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048"""

from collections import Counter


def scramble(s1: str, s2: str):
    c1, c2 = Counter(s1), Counter(s2)
    return not bool(c2 - c1)
