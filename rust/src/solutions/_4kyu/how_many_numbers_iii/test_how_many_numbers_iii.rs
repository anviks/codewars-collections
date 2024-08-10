/*
 * https://www.codewars.com/kata/5877e7d568909e5ff90017e6
 */

// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::super::solution_how_many_numbers_iii::find_all;

    #[test]
    fn sample_tests() {
        assert_eq!(find_all(10, 3), Some((8, 118, 334)));
        assert_eq!(find_all(27, 3), Some((1, 999, 999)));
        assert_eq!(find_all(84, 4), None);
        assert_eq!(find_all(35, 6), Some((123, 116999, 566666)));
    }

    #[test]
    fn performance_test_find_all_1() {
        assert_eq!(find_all(13, 3), Some((12, 139, 445)));
    }

    #[test]
    fn performance_test_find_all_2() {
        assert_eq!(find_all(13, 6), Some((14, 111118, 222223)));
    }

    #[test]
    fn performance_test_find_all_3() {
        assert_eq!(find_all(13, 8), Some((7, 11111116, 11122222)));
    }
}


