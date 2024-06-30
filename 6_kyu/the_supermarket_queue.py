"""https://www.codewars.com/kata/57b06f90e298a7b53d000a86"""


def queue_time(customers: list[int], n: int):
    result = 0
    
    while customers:
        customers[:n] = [m - 1 for m in customers[:n] if m - 1 > 0]
        result += 1
        
    return result


def main():
    print(queue_time([], 1), 0)
    print(queue_time([5], 1), 5)
    print(queue_time([2], 5), 2)
    print(queue_time([1, 2, 3, 4, 5], 1), 15)
    print(queue_time([1, 2, 3, 4, 5], 100), 5)
    print(queue_time([2, 2, 3, 3, 4, 4], 2), 9)


if __name__ == '__main__':
    main()
