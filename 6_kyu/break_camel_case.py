"""https://www.codewars.com/kata/5208f99aee097e6552000148"""


def solution(s):
    return __import__('re').sub(r'(?=[A-Z])', ' ', s)


def main():
    print(solution('camelCase'))


if __name__ == '__main__':
    main()
