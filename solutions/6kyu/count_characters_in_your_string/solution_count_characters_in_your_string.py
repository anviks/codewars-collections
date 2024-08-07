"""https://www.codewars.com/kata/52efefcbcdf57161d4000091"""

import collections


def count(s: str):
    return collections.Counter(s)


def count2(s: str):
    return {c: s.count(c) for c in set(s)}
