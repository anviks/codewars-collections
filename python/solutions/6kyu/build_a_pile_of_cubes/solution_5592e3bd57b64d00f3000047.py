"""https://www.codewars.com/kata/5592e3bd57b64d00f3000047"""


def find_nb(m):
    for i in range(1, m):
        m -= i ** 3

        if m == 0:
            return i
        elif m < 0:
            return -1
