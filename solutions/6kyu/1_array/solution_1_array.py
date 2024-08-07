"""https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9"""


def up_array(arr: list[int]) -> list[int] | None:
    if any(n < 0 or n > 9 for n in arr):
        return None

    num = int(''.join(str(d) for d in arr)) + 1

    return [int(d) for d in str(num).zfill(len(arr))]
