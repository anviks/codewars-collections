"""https://www.codewars.com/kata/64607242d3560e0043c3de25"""

from math import ceil, floor

from utils_anviks import stopwatch


@stopwatch
def count_palindromes(start, end):
    start, end = ceil(start), floor(end)

    if end < start:
        return 0

    def count_palindromes_with_length(n):
        if n == 1:
            return 9  # Palindromes: 1, 2, ..., 9
        half_length = (n + 1) // 2
        return 9 * (10 ** (half_length - 1))

    def count_up_to(limit):
        if limit < 0:
            return 0
        limit_str = str(limit)
        length = len(limit_str)
        count = 0

        for l in range(1, length):
            count += count_palindromes_with_length(l)

        half_length = (length + 1) // 2
        half_part = int(limit_str[:half_length])
        first_half_palindromes = range(10 ** (half_length - 1), half_part + 1)

        for half in first_half_palindromes:
            pal_str = str(half)
            if length % 2 == 0:
                pal = int(pal_str + pal_str[::-1])
            else:
                pal = int(pal_str + pal_str[-2::-1])

            if pal > limit:
                break
            count += 1

        return count

    return count_up_to(end) - count_up_to(start - 1) + (start == 0)
