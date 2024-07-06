"""https://www.codewars.com/kata/5511b2f550906349a70004e1"""


def last_digit(n1: int, n2: int) -> int:
    if n2 == 0:
        return 1  # Any number to the power of 0 is 1
    
    # Reduce n to its last digit
    last_digit_n1 = n1 % 10

    # Patterns for the last digit cycles
    cycles = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    # Get the cycle for the last digit
    cycle = cycles[last_digit_n1]
    cycle_length = len(cycle)

    # Reduce the exponent m modulo the cycle length
    reduced_exponent = n2 % cycle_length

    # If reduced_exponent is 0, it means we need the last element in the cycle
    if reduced_exponent == 0:
        reduced_exponent = cycle_length

    # The last digit of n^m is the (reduced_exponent - 1)-th element in the cycle
    return cycle[reduced_exponent - 1]


def main():
    from util_funcs import pretty_compare

    for n1, n2, exp in [
        (4, 1, 4),
        (4, 2, 6),
        (9, 7, 9),
        (10, 10 ** 10, 0),
        (2 ** 200, 2 ** 300, 6),
        (3715290469715693021198967285016729344580685479654510946723,
         68819615221552997273737174557165657483427362207517952651, 7),
    ]:
        pretty_compare(last_digit(n1, n2), exp)


if __name__ == '__main__':
    main()
