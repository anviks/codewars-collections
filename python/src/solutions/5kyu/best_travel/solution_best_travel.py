"""https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa"""

from itertools import combinations


def choose_best_sum(t: int, k: int, ls: list[int]) -> int | None:
    return max((s for c in combinations(ls, k) if (s := sum(c)) <= t), default=None)
