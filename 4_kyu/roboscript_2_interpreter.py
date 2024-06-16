"""https://www.codewars.com/kata/58738d518ec3b4bf95000192"""
import re


def expand_commands(match) -> str:
    group_one = match.group(1)
    group_two = int(match.group(2))
    return group_one * group_two


def execute(code: str) -> str:
    pattern = re.compile(r'\(([FRL\d]+)\)(\d+)')

    while pattern.search(code):
        code = pattern.sub(expand_commands, code)
        
    print(code)
        
    return roboscript_1_execute(code)
    

def roboscript_1_execute(code: str) -> str:
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
    print(execute('R9FR7R1L8((F3RF5L)0R(F7LF6LF1R6)8LR1F(F1LF2LF9R8)10R2L1R)5L8F4LL8F'))
    # execute("RL66RRFR7F73R69FFFFFLRRR71FRRL34R81FLR97F20LL61RLL5R17LF26F84FR71L83F26FRR46FF16FR22LLL1RRR49F71RRR54L50RF75LL94FRL98FF55FLL28R71R8FRFFF86LRR50RRR50FFL10R23FR97L9LFLFFFFLRL8R")
    # execute("F5LF5LF5LF5L")
    
    
    # F4LF4RF4RF4LF4LF4RF4RF4LF4LF4RF4RF4
    # F4L((F4R)2(F4L)2)2(F4R)2F4    


if __name__ == '__main__':
    main()
