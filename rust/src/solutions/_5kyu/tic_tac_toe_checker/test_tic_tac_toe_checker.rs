/*
 * https://www.codewars.com/kata/525caa5c1bf619d28c000335
 */

use super::solution_tic_tac_toe_checker::*;

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::is_solved;
        
    fn dotest(board: &[&[u8; 3]; 3], expected: i8) {
        let actual = is_solved(board);
        assert_eq!(actual, expected, "With board = {board:?}\nExpected {expected} but got {actual}")
    }

    #[test]
    fn fixed_tests() {
        for (board, expected) in [
            ([&[0, 0, 1], &[0, 1, 2], &[2, 1, 0]], -1),
            ([&[1, 1, 1], &[0, 2, 2], &[0, 0, 0]], 1),
            ([&[2, 1, 2], &[2, 1, 1], &[1, 1, 2]], 1),
            ([&[2, 1, 2], &[2, 1, 1], &[1, 2, 1]], 0)
        ] {
            dotest(&board, expected);
        }
    }
}
