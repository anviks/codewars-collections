"""
https://www.codewars.com/kata/53f40dff5f9d31b813000774

**Recover a secret string from random triplets**

There is a secret string which is unknown to you. Given a collection of random triplets from the string,
recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before
the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets
and that they contain sufficient information to deduce the original string. In particular,
this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
"""


def recover_secret(triplets):
    result = ""
    first_letters = {t[0] for t in triplets}

    for trip in triplets:
        for i in range(1, 3):
            first_letters.discard(trip[i])

    result += first_letters.pop()

    while (next_letter := __get_next_letter(result, triplets)) != "":
        result += next_letter

    return result


def __get_next_letter(result, triplets) -> str:
    potential_next_letters = {letter for trip in triplets for letter in trip}.difference(set(result))
    for trip in triplets:
        for i in range(2):
            if trip[1 - i] not in result:
                potential_next_letters.discard(trip[2 - i])

    return potential_next_letters.pop() if len(potential_next_letters) == 1 else ""


if __name__ == '__main__':
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]

    print(recover_secret(triplets))  # whatisup

    triplets = [
        ['t', 's', 'f'],
        ['a', 's', 'u'],
        ['m', 'a', 'f'],
        ['a', 'i', 'n'],
        ['s', 'u', 'n'],
        ['m', 'f', 'u'],
        ['a', 't', 'h'],
        ['t', 'h', 'i'],
        ['h', 'i', 'f'],
        ['m', 'h', 'f'],
        ['a', 'u', 'n'],
        ['m', 'a', 't'],
        ['f', 'u', 'n'],
        ['h', 's', 'n'],
        ['a', 'i', 's'],
        ['m', 's', 'n'],
        ['m', 's', 'u']
    ]

    print(recover_secret(triplets))  # mathisfun

    triplets = [
        ['g', 'a', 's'],
        ['o', 'g', 's'],
        ['c', 'n', 't'],
        ['c', 'o', 'n'],
        ['a', 't', 's'],
        ['g', 'r', 't'],
        ['r', 't', 's'],
        ['c', 'r', 'a'],
        ['g', 'a', 't'],
        ['n', 'g', 's'],
        ['o', 'a', 's']
    ]

    print(recover_secret(triplets))  # congrats
