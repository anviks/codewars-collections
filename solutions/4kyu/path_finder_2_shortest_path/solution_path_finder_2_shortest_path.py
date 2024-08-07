"""https://www.codewars.com/kata/57658bfa28ed87ecfa00058a"""

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
