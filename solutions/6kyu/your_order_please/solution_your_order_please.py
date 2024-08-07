"""https://www.codewars.com/kata/55c45be3b2079eccff00010f"""

import re


def order(sentence: str):
    return ' '.join(sorted(sentence.split(), key=lambda word: int(re.search(r'^.*(\d).*$', word).group(1))))
