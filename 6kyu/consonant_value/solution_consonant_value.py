"""https://www.codewars.com/kata/59c633e7dcc4053512000073"""

import re


def solve(s: str):
    return max(
        sum(ord(c) - 96 for c in m)
        for m in re.findall(r'[b-df-hj-np-tv-z]+', s)
    )
