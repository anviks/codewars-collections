/*
 * https://www.codewars.com/kata/55b195a69a6cc409ba000053
 */

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html
#[cfg(test)]
mod tests {
    use crate::solutions::_4kyu
    ::total_increasing_or_decreasing_numbers_up_to_a_power_of_10
    ::solution_total_increasing_or_decreasing_numbers_up_to_a_power_of_10
    ::total_inc_dec;

    fn dotest(n: u32, expected: u64) {
        let actual = total_inc_dec(n);
        assert_eq!(actual, expected, "With n = {n}\nExpected {expected} but got {actual}")
    }

    #[test]
    fn fixed_tests() {
        dotest(0, 1);
        dotest(1, 10);
        dotest(2, 100);
        dotest(3, 475);
        dotest(4, 1675);
    }
}

