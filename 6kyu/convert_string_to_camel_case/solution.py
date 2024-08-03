"""https://www.codewars.com/kata/517abf86da9663f1d2000003"""

import re

to_camel_case = lambda text: re.sub(r"[-_].", lambda m: m[0][1].upper(), text)
