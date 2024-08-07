"""https://www.codewars.com/kata/53697be005f803751e0015aa"""

import re


def encode(st: str):
    return re.sub(r'[aeiou]', lambda m: str('aeiou'.index(m.group()) + 1), st)


def decode(st: str):
    return re.sub(r'[1-5]', lambda m: 'aeiou'[int(m.group()) - 1], st)
