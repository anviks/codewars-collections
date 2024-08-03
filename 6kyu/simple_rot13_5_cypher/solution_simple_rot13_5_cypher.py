"""https://www.codewars.com/kata/5894986e2ddc8f6805000036"""

import re
from codecs import encode


def rot_135(st):
    return re.sub(r'\d', lambda m: str((int(m.group()) + 5) % 10), encode(st, 'rot13'))
