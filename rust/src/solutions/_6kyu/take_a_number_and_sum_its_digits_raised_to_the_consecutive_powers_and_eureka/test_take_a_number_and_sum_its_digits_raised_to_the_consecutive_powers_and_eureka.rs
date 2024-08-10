/*
 * https://www.codewars.com/kata/5626b561280a42ecc50000d1
 */

use super::solution_take_a_number_and_sum_its_digits_raised_to_the_consecutive_powers_and_eureka::*;

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::sum_dig_pow;
        
    fn dotest(a: u64, b: u64, expected: &[u64]) {
        let actual = sum_dig_pow(a, b);
        assert_eq!(actual, expected, "With a = {a}, b = {b}\nExpected {expected:?} but got {actual:?}")
    }

    #[test]
    fn sample_tests() {
        dotest(1, 10, &[1, 2, 3, 4, 5, 6, 7, 8, 9]);
        dotest(1, 100, &[1, 2, 3, 4, 5, 6, 7, 8, 9, 89]);
        dotest(10, 89, &[89]);
        dotest(10, 100, &[89]);
        dotest(90, 100, &[]);
        dotest(89, 135, &[89, 135]);
    }
}
