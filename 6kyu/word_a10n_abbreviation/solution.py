"""https://www.codewars.com/kata/5375f921003bf62192000746"""

import re


def shortener(m: re.Match) -> str:
    s = m.group()
    return s[0] + str(len(s) - 2) + s[-1]


def abbreviate(s: str):
    return re.sub(r'[a-zA-Z]{4,}', shortener, s)
