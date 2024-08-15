"""https://www.codewars.com/kata/strip-comments"""

import re


def strip_comments(s, m):
    return re.sub(fr'[ \t]*[{re.escape("".join(m))}].*', '', s) if m else s
