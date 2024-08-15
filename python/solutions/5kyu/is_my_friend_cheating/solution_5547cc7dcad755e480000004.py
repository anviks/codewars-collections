"""https://www.codewars.com/kata/5547cc7dcad755e480000004"""


def remov_nb(n: int):
    r = range(1, n + 1)
    range_sum = sum(r)
    combs = []

    for a in r:
        b = (range_sum - a) / (a + 1)
        if b.is_integer() and 1 <= b <= n:
            combs.append((a, int(b)))

    return combs
