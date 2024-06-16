"""
https://www.codewars.com/kata/5679d5a3f2272011d700000d

## 6 by 6 Skyscrapers

In a grid of 6 by 6 squares you want to place a skyscraper in each square with only some clues:

- The height of the skyscrapers is between 1 and 6
- No two skyscrapers in a row or column may have the same number of floors
- A clue is the number of skyscrapers that you can see in a row or column from the outside
- Higher skyscrapers block the view of lower skyscrapers located behind them
"""


def solve_puzzle(clues):
    pass


if __name__ == '__main__':
    clues = (
        3, 2, 2, 3, 2, 1,
        1, 2, 3, 3, 2, 2,
        5, 1, 2, 2, 4, 3,
        3, 2, 1, 2, 2, 4
    )
    actual = solve_puzzle(clues)
    expected = (
        (2, 1, 4, 3, 5, 6),
        (1, 6, 3, 2, 4, 5),
        (4, 3, 6, 5, 1, 2),
        (6, 5, 2, 1, 3, 4),
        (5, 4, 1, 6, 2, 3),
        (3, 2, 5, 4, 6, 1)
    )
