"""https://www.codewars.com/kata/53f40dff5f9d31b813000774"""


def recover_secret(triplets):
    result = ""
    first_letters = {t[0] for t in triplets}

    for trip in triplets:
        for i in range(1, 3):
            first_letters.discard(trip[i])

    result += first_letters.pop()

    while (next_letter := _get_next_letter(result, triplets)) != "":
        result += next_letter

    return result


def _get_next_letter(result, triplets) -> str:
    potential_next_letters = {letter for trip in triplets for letter in trip}.difference(set(result))
    for trip in triplets:
        for i in range(2):
            if trip[1 - i] not in result:
                potential_next_letters.discard(trip[2 - i])

    return potential_next_letters.pop() if len(potential_next_letters) == 1 else ""

