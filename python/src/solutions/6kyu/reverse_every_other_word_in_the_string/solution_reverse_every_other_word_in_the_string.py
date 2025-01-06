"""https://www.codewars.com/kata/58d76854024c72c3e20000de"""

import re


def reverse_alternate(st: str):
    words = re.split(' +', st.strip())
    for i in range(len(words)):
        if i % 2:
            words[i] = words[i][::-1]
    return ' '.join(words)
