"""https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa"""
from itertools import combinations


def choose_best_sum(t: int, k: int, ls: list[int]) -> int | None:
    return max((s for c in combinations(ls, k) if (s := sum(c)) <= t), default=None)


def main():
    from util_funcs import pretty_compare

    ts = [50, 55, 56, 57, 58]
    pretty_compare(choose_best_sum(163, 3, ts), 163)

    ts = [50]
    pretty_compare(choose_best_sum(163, 3, ts), None)

    ts = [91, 74, 73, 85, 73, 81, 87]
    pretty_compare(choose_best_sum(230, 3, ts), 228)
    pretty_compare(choose_best_sum(331, 2, ts), 178)
    pretty_compare(choose_best_sum(331, 4, ts), 331)
    pretty_compare(choose_best_sum(331, 5, ts), None)
    pretty_compare(choose_best_sum(331, 1, ts), 91)
    pretty_compare(choose_best_sum(700, 6, ts), 491)


if __name__ == '__main__':
    main()
