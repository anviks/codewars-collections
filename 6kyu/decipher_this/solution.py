"""https://www.codewars.com/kata/581e014b55f2c52bb00000f8"""

import re


def decipher_this(s: str):
    result = []

    for word in s.split():
        digits = re.search(r'^\d+', word).group()
        m_len = len(digits)
        new_word = chr(int(digits))

        if len(word) < m_len + 2:
            result.append(new_word + word[m_len:])
        else:
            result.append(new_word + word[-1] + word[m_len + 1:-1] + word[m_len])

    return ' '.join(result)
