"""https://www.codewars.com/kata/564057bc348c7200bd0000ff"""


def thirt(n: int) -> int:
    remainders = [1, 10, 9, 12, 3, 4]

    while True:
        str_n = str(n)[::-1]
        new_n = 0

        for i, d in enumerate(str_n):
            new_n += int(d) * remainders[i % len(remainders)]

        if n == new_n: break
        n = new_n

    return new_n
