"""https://www.codewars.com/kata/5629db57620258aa9d000014"""

from collections import Counter


def get_counter(string: str):
    counter = Counter(c for c in string if c.islower())
    counter = Counter({k: v for k, v in counter.items() if v > 1})

    return counter


def mix(s1: str, s2: str) -> str:
    counter1, counter2 = get_counter(s1), get_counter(s2)
    all_characters = set(s1) | set(s2)
    result: list[str] = []

    for char in all_characters:
        char_result: str = char * max(counter1[char], counter2[char])

        if char in counter1 or char in counter2:
            if counter1[char] > counter2[char]:
                char_result = '1:' + char_result
            elif counter1[char] < counter2[char]:
                char_result = '2:' + char_result
            else:
                char_result = '=:' + char_result
        else:
            continue

        result.append(char_result)

    result.sort(key=lambda x: (-len(x), x))

    return '/'.join(result)
