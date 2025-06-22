"""https://www.codewars.com/kata/549ee8b47111a81214000941"""
from collections import deque

jump_directions = [
    2 + 1j,
    2 + -1j,
    -2 + 1j,
    -2 + -1j,
    1 + 2j,
    1 + -2j,
    -1 + 2j,
    -1 + -2j,
]

def knight(p1: str, p2: str):
    start = (ord(p1[0]) - ord('a')) * 1j + int(p1[1])
    target = (ord(p2[0]) - ord('a')) * 1j + int(p2[1])

    return calculate_jumps(start, target)


def calculate_jumps(start: complex, target: complex):
    queue = deque([(start, 0)])

    while queue:
        square, jumps = queue.popleft()

        if square == target:
            return jumps

        for direction in jump_directions:
            queue.append((square + direction, jumps + 1))
