"""https://www.codewars.com/kata/5420fc9bb5b2c7fd57000004"""


def highest_rank(arr):
    return max(set(arr), key=lambda x: (arr.count(x), x))
