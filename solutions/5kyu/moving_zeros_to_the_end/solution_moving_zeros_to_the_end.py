"""https://www.codewars.com/kata/52597aa56021e91c93000cb0"""


def move_zeros(lst: list[int]):
    return [n for n in lst if n != 0] + [0] * lst.count(0)
