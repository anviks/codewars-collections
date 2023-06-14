"""
https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/python

**Multiplication table**

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9

For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""


def multiplication_table(size):
    return [[i * j for i in range(1, size + 1)] for j in range(1, size + 1)]


if __name__ == '__main__':
    print(multiplication_table(2))  # [[1,2], [2,4]]
    print(multiplication_table(3))  # [[1,2,3], [2,4,6], [3,6,9]]
    print(multiplication_table(4))  # [[1,2,3,4], [2,4,6,8], [3,6,9,12], [4,8,12,16]]
    print(multiplication_table(5))  # [[1,2,3,4,5], [2,4,6,8,10], [3,6,9,12,15], [4,8,12,16,20], [5,10,15,20,25]]
