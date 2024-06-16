"""https://www.codewars.com/kata/5870fa11aa0428da750000da"""
import re

from utils_anviks import stopwatch


@stopwatch
def execute(code: str):
    mapper = {'R': 1j, 'L': -1j}
    location = 0
    direction = 1j
    visited: set[complex] = {location}

    for char, multiplier in re.findall(r"([FLR])(\d*)", code):
        multiplier = int(multiplier or 1)

        for _ in range(multiplier):
            if char == 'F':
                location += direction
                visited.add(location)
            else:
                direction /= mapper[char]

    coords = set(map(lambda im: (int(im.real), int(im.imag)), visited))

    min_x = min(coords)[0]
    min_y = min(coords, key=lambda c: c[1])[1]
    max_x = max(coords)[0]
    max_y = max(coords, key=lambda c: c[1])[1]

    matrix = [['*' if complex(x, y) in visited else ' ' for y in range(min_y, max_y + 1)] for x in
              range(min_x, max_x + 1)]

    return '\r\n'.join(''.join(line) for line in matrix)

def main():
    execute("RL66RRFR7F73R69FFFFFLRRR71FRRL34R81FLR97F20LL61RLL5R17LF26F84FR71L83F26FRR46FF16FR22LLL1RRR49F71RRR54L50RF75LL94FRL98FF55FLL28R71R8FRFFF86LRR50RRR50FFL10R23FR97L9LFLFFFFLRL8R")
    execute("F5LF5LF5LF5L")
    

if __name__ == '__main__':
    main()
