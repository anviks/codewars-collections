"""https://www.codewars.com/kata/52761ee4cffbc69732000738"""


def good_vs_evil(good: str, evil: str) -> str:
    good_values = [1, 2, 3, 3, 4, 10]
    evil_values = [1, 2, 2, 2, 3, 5, 10]
    good_army = parse_army_value(good, good_values)
    evil_army = parse_army_value(evil, evil_values)

    if good_army > evil_army:
        return 'Battle Result: Good triumphs over Evil'
    if good_army < evil_army:
        return 'Battle Result: Evil eradicates all trace of Good'

    return 'Battle Result: No victor on this battle field'


def parse_army_value(counts: str, values: list[int]) -> int:
    acc = 0
    for i, count in enumerate(int(c) for c in counts.split()):
        acc += values[i] * count
    return acc
