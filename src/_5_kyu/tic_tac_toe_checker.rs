/**
# [Tic-Tac-Toe Checker](https://www.codewars.com/kata/525caa5c1bf619d28c000335)

If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we?
Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is `0` if a spot is empty,
`1` if it is an `"X"`, or `2` if it is an `"O"`, like so:

```rust
[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
```

We want our function to return:

- `-1` if the board is not yet finished (there are empty spots),
- `1` if "X" won,
- `2` if "O" won,
- `0` if it's a cat's game (i.e. a draw).

You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
 */
use std::time::Instant;


macro_rules! check_winner {
    ($square1:expr, $square2:expr, $square3:expr) => {
        if $square1 == $square2 && $square2 == $square3 && $square1 != 0 {
            return $square1 as i8
        }
    };
}

fn is_solved(board: &[&[u8; 3]; 3]) -> i8 {
    let mut has_empty = false;

    for i in 0..3 {
        let row = board[i];

        if row.contains(&0) { has_empty = true }

        check_winner!(row[0], row[1], row[2]);
        check_winner!(board[0][i], board[1][i], board[2][i]);
    }

    for i in [0, 2] {
        check_winner!(board[0][0 + i], board[1][1], board[2][2 - i]);
    }

    if has_empty { -1 } else { 0 }
}

pub fn main() {
    let start = Instant::now();
    println!("{}", is_solved(&[&[0, 0, 1], &[0, 1, 2], &[2, 1, 0]]));  // -1
    println!("{}", is_solved(&[&[1, 1, 1], &[0, 2, 2], &[0, 0, 0]]));  // 1
    println!("{}", is_solved(&[&[2, 2, 2], &[0, 1, 1], &[1, 0, 0]]));  // 2
    println!("{}", is_solved(&[&[2, 1, 2], &[2, 1, 1], &[1, 2, 1]]));  // 0

    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[2, 1, 2]]));  // 0
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[1, 2, 1]]));  // 1
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[1, 2, 2]]));  // 1
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[1, 1, 2]]));  // 1

    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[1, 2, 0]]));  // 1
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[0, 2, 1]]));  // 1
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[0, 0, 1]]));  // 1
    println!("{}", is_solved(&[&[1, 2, 1], &[2, 1, 2], &[0, 1, 0]]));  // -1

    println!("{}", is_solved(&[&[0, 1, 1], &[2, 0, 2], &[2, 1, 0]]));  // -1
    println!("{}", is_solved(&[&[0, 2, 0], &[0, 0, 2], &[1, 1, 0]]));  // -1
    let duration = start.elapsed();

    println!("Time elapsed: {:?}", duration);
    // 45 - 71 microseconds without macro
    // 44 - 83 microseconds with macro
}
