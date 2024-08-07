"""https://www.codewars.com/kata/5263c6999e0f40dee200059d"""

from itertools import product


def get_pins(observed: str) -> list[str]:
    possibilities: list[list[str]] = []

    for digit in observed:
        num = int(digit) or 11
        digit_possibilities = [digit]

        for neighbour in [num - 3, num - 1, num + 1, num + 3]:
            if neighbour <= 0:
                continue
            if neighbour == 11:
                neighbour = 0
            if neighbour >= 10:
                continue
            # This condition eliminates 'false' neighbours like 6 and 7
            if (neighbour % 3) ^ (num % 3) == 1:
                continue

            digit_possibilities.append(str(neighbour))

        possibilities.append(digit_possibilities)

    return [''.join(p) for p in product(*possibilities)]
