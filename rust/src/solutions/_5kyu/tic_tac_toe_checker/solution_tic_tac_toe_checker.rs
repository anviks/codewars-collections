/*
 * https://www.codewars.com/kata/525caa5c1bf619d28c000335
 */

macro_rules! check_winner {
    ($square1:expr, $square2:expr, $square3:expr) => {
        if $square1 == $square2 && $square2 == $square3 && $square1 != 0 {
            return $square1 as i8;
        }
    };
}

pub fn is_solved(board: &[&[u8; 3]; 3]) -> i8 {
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

