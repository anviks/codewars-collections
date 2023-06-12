import alternate_1
import alternate_2
import alternate_3
import alternate_4
import alternate_5


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
    print(alternate_1.recover_secret(triplets))
    print(alternate_2.recover_secret(triplets))
    print(alternate_3.recover_secret(triplets))
    print(alternate_4.recover_secret(triplets))
    print(alternate_5.recover_secret(triplets))
