"""https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2"""


def validate(n: int) -> bool:
    digits = [int(d) for d in str(n)]
    
    for i in range(len(digits) - 2, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9

    return not sum(digits) % 10


def main():
    from util_funcs import pretty_compare

    pretty_compare(validate(1714), False)
    pretty_compare(validate(12345), False)
    pretty_compare(validate(891), False)
    pretty_compare(validate(123), False)
    pretty_compare(validate(1), False)
    pretty_compare(validate(2121), True)
    pretty_compare(validate(1230), True)


if __name__ == '__main__':
    main()
