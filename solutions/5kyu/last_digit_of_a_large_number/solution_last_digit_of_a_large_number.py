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
