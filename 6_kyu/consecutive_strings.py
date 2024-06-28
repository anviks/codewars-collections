"""https://www.codewars.com/kata/56a5d994ac971f1ac500003e"""


def longest_consec(strarr, k):
    candidates = [''.join(t) for t in zip(*(strarr[i:] for i in range(k)))]  # Because sliding window is old and boring
    return max(candidates, key=lambda s: len(s), default='')


def main():
    print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")
    print(longest_consec([], 3), "")


if __name__ == '__main__':
    main()

