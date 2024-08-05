"""https://www.codewars.com/kata/simple-encryption-number-2-index-difference"""

from string import ascii_lowercase, ascii_uppercase, digits

REGION = ascii_uppercase + ascii_lowercase + digits + '''.,:;-?! '()$%&"'''


def encrypt(text: str) -> str:
    if not text:
        return text

    chars = list(text)

    for i, c in enumerate(chars):
        if c not in REGION:
            raise ValueError('Invalid character')
        if i % 2 == 1:
            chars[i] = c.swapcase()

    for i in range(len(chars) - 1, 0, -1):
        new_index = (REGION.index(chars[i - 1]) - REGION.index(chars[i]) + len(REGION)) % len(REGION)
        chars[i] = REGION[new_index]

    first_index = REGION.index(chars[0])
    chars[0] = REGION[-first_index - 1]

    return ''.join(chars)


def decrypt(text: str) -> str:
    if not text:
        return text

    chars = list(text)

    first_index = REGION.index(chars[0])
    chars[0] = REGION[-first_index - 1]

    for i in range(1, len(chars)):
        new_index = (REGION.index(chars[i - 1]) - REGION.index(chars[i]) + len(REGION)) % len(REGION)
        chars[i] = REGION[new_index]

    for i, c in enumerate(chars):
        if i % 2 == 1:
            chars[i] = c.swapcase()

    return ''.join(chars)
