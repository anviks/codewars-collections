/*
 * https://www.codewars.com/kata/51e0007c1f9378fa810002a9
 */

use super::solution_make_the_deadfish_swim::*;

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn sample_tests() {
        assert_eq!(parse("iiisdoso"),
            vec![8, 64]);
        assert_eq!(parse("iiisdosodddddiso"),
            vec![8, 64, 3600]);
    }
}
