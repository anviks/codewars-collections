"""https://www.codewars.com/kata/one-line-task-palindrome-string"""


palindrome=lambda n,c:c+c[-1]*(n-len(c)*2+1)+c[-2::-1]


def main():
    print(len(palindrome(11, 'ab')))
    print(len(palindrome(20, 'abcd')))
    print((palindrome(11, 'ab')))
    print((palindrome(20, 'abcd')))


if __name__ == '__main__':
    main()
