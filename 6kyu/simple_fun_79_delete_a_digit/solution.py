"""https://www.codewars.com/kata/5894318275f2c75695000146"""


def delete_digit(n: int) -> int:
    str_n = str(n)
    return max(int(str_n[:i] + str_n[i + 1:]) for i in range(len(str_n)))
