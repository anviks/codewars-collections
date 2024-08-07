"""https://www.codewars.com/kata/5202ef17a402dd033c000009"""


def title_case(title: str, minor_words=''):
    minor_words = set(minor_words.lower().split())
    words = title.lower().split()

    for i, word in enumerate(words):
        if word in minor_words and i != 0:
            continue

        words[i] = word.capitalize()

    return ' '.join(words)
