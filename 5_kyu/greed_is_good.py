"""https://www.codewars.com/kata/5270d0d18625160ada0000e4"""
from collections import Counter


def score(dice: list[int]) -> int:
    triple_points = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    single_points = {1: 100, 5: 50}
    counts = Counter(dice)
    total = 0
    
    for k, v in counts.items():
        if v >= 3:
            total += triple_points[k]
            v -= 3
        total += single_points.get(k, 0) * v
        
    return total


def main():
    print(score([5, 1, 3, 4, 1]), 250)
    print(score([1, 1, 1, 3, 1]), 1100)
    print(score([2, 3, 4, 6, 2]), 0)
    print(score([4, 4, 4, 3, 3]), 400)
    print(score([2, 4, 4, 5, 4]), 450)


if __name__ == '__main__':
    main()
