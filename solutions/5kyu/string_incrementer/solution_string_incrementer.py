"""https://www.codewars.com/kata/54a91a4883a7de5d7800009c"""

import re


def increment_string(strng):
    m = re.search(r'^(.*?)(\d*)$', strng)
    p1, p2 = m.groups()
    return p1 + str(int(p2 or 0) + 1).zfill(len(p2))
