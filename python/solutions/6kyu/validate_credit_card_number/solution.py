"""https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2"""


def validate(n: int) -> bool:
    digits = [int(d) for d in str(n)]

    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return not sum(digits) % 10
