"""https://www.codewars.com/kata/5727bb0fe81185ae62000ae3"""


def clean_string(s: str):
    cleaned = []

    for char in s:
        if char == '#':
            cleaned and cleaned.pop()
        else:
            cleaned.append(char)

    return ''.join(cleaned)
