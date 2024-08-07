"""https://www.codewars.com/kata/576986639772456f6f00030c"""

from collections import deque


def path_finder(area: str):
    area = area.split()

    N = len(area)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up

    start = (0, 0)
    end = (N - 1, N - 1)

    #                 v-- current point
    #                      v-- climbed
    #                            v-- visited
    paths = deque([(start, 0, {start})])
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

                paths.append((new_location, new_height_climbed, new_visited))

    return shortest_path
