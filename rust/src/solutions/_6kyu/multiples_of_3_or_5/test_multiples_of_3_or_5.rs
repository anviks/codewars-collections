/*
 * https://www.codewars.com/kata/514b92a657cdc65150000006
 */

use super::solution_multiples_of_3_or_5::*;

mod tests {
    use super::solution;

    #[test]
    fn sample_tests() {
        // assertion(expected, input);
        assertion(23, 10);
        assertion(33, 11);
        assertion(225, 33);
        assertion(8, 6);
        assertion(3420, 123);
        assertion(543, 50);
        assertion(0, 0);
        assertion(0, -203);
        assertion(25719750, 10500);
    }

    fn assertion(expected: i32, input: i32) {
        let actual = solution(input);

        assert_eq!(
            expected,
            actual,
            "\nTest failed!\n expected: {}\n actual: {}\n input: {}\n",
            expected,
            actual,
            input
        );
    }
}
