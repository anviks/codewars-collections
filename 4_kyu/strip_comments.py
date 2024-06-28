"""https://www.codewars.com/kata/strip-comments"""

import re

def strip_comments(s, m):
    return re.sub(fr'[ \t]*[{re.escape("".join(m))}].*', '', s) if m else s


def main():
    result = strip_comments("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
    print(result == "apples, pears\ngrapes\nbananas")


if __name__ == '__main__':
    main()
