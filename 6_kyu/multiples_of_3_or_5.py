"""
https://www.codewars.com/kata/514b92a657cdc65150000006'

**Multiples of 3 or 5**

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.
"""


solution = lambda n: sum(i for i in range(n) if not i % 3 or not i % 5)


if __name__ == '__main__':
    print(solution(10))  # 23
    print(solution(20))  # 78
    print(solution(200))  # 9168
