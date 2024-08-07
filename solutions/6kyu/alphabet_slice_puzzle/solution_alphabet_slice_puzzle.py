"""https://www.codewars.com/kata/660d55d0ba01e5016c85cfeb"""

import functools as f

slice = lambda a, b: f.reduce(lambda c, d: c + d, map(chr, range(ord(a), ord(b) + 1)))
