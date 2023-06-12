"""
https://www.codewars.com/kata/576986639772456f6f00030c

Path Finder #3: the Alpinist

Task
You are at start location [0, 0] in mountain area of NxN and you can only move in one of the four cardinal directions
(i.e. North, East, South, West). Return minimal number of climb rounds to target location [N-1, N-1].
Number of climb rounds between adjacent locations is defined as difference of location altitudes (ascending or descending).

Location altitude is defined as an integer number (0-9).

Path Finder Series:
#1: can you reach the exit?
#2: shortest path
#3: the Alpinist
#4: where are you?
#5: there's someone here
"""
import time
from collections import deque


def path_finder(area: str):
    area = area.split()

    N = len(area)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    start = (0, 0)
    end = (N - 1, N - 1)

    #           v-- current point
    #                v-- climbed
    #                    v-- visited
    paths = deque([[start, 0, {start}]])
    shortest_path = float('inf')

    while paths:
        current_path = paths.popleft()
        location, height_climbed, visited = current_path
        row, col = location

        if location == end:
            shortest_path = min(shortest_path, height_climbed)
            continue

        if height_climbed >= shortest_path:
            continue

        for x, y in directions:
            new_row, new_col = row + x, col + y
            new_location = (new_row, new_col)

            if 0 <= new_row < N and 0 <= new_col < N and new_location not in visited:
                new_height_climbed = height_climbed + abs(int(area[row][col]) - int(area[new_row][new_col]))
                new_visited = visited.copy()
                new_visited.add(new_location)

                paths.append([new_location, new_height_climbed, new_visited])

    return shortest_path


if __name__ == '__main__':
    a = "\n".join([
        "000",
        "000",
        "000"
    ])
    print(path_finder(a))  # 0

    b = "\n".join([
        "010",
        "010",
        "010"
    ])
    print(path_finder(b))  # 2

    c = "\n".join([
        "010",
        "101",
        "010"
    ])
    print(path_finder(c))  # 4

    d = "\n".join([
        "0707",
        "7070",
        "0707",
        "7070"
    ])
    print(path_finder(d))  # 42

    e = "\n".join([
        "700000",
        "077770",
        "077770",
        "077770",
        "077770",
        "000007"
    ])
    print(path_finder(e))  # 14

    f = "\n".join([
        "777000",
        "007000",
        "007000",
        "007000",
        "007000",
        "007777"
    ])
    print(path_finder(f))  # 0

    st = time.perf_counter()
    g = "\n".join([
        "000000",
        "000000",
        "000000",
        "000010",
        "000109",
        "001010"
    ])
    print(path_finder(g))  # 4
    # Original solution: 20.784861400003138
    # Deque solution: 7.182043999997404
    print(time.perf_counter() - st)
