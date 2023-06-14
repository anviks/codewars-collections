"""
https://www.codewars.com/kata/57658bfa28ed87ecfa00058a

**Path Finder #2: shortest path**

Task
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West).
Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position.
Otherwise, return false.

Empty positions are marked ..
Walls are marked W.
Start and exit positions are guaranteed to be empty in all test cases.

Path Finder Series:
#1: can you reach the exit?
#2: shortest path
#3: the Alpinist
#4: where are you?
#5: there's someone here
"""

from collections import deque


def path_finder(maze):
    maze = maze.split("\n")

    N = len(maze)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    start = (0, 0)
    target = (N - 1, N - 1)

    visited = set()
    visited.add(start)

    queue = deque([(start, 0)])  # (position, steps)

    while queue:
        current, steps = queue.popleft()
        if current == target:
            return steps

        x, y = current
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N and maze[new_x][new_y] == "." and (new_x, new_y) not in visited:
                visited.add((new_x, new_y))
                queue.append(((new_x, new_y), steps + 1))

    return False


if __name__ == '__main__':
    a = "\n".join([
        ".W.",
        ".W.",
        "..."
    ])
    print(path_finder(a))  # 4

    b = "\n".join([
        ".W.",
        ".W.",
        "W.."
    ])
    print(path_finder(b))  # False

    c = "\n".join([
        "......",
        "......",
        "......",
        "......",
        "......",
        "......"
    ])
    print(path_finder(c))  # 10

    d = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
    ])
    print(path_finder(d))  # False
