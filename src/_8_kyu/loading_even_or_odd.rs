/*
 * https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/rust
 */


fn even_or_odd(number: i32) -> &'static str {
    return if number % 2 == 0 { "Even" } else { "Odd" };
}


// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod sample_tests {
    use super::even_or_odd;

    fn do_test(number: i32, expected: &str) {
        let actual = even_or_odd(number);
        assert_eq!(actual, expected, "\nYour result (left) does not match the expected output (right) for the input {number:?}");
    }

    #[test]
    fn test_zero() {
        do_test(0, "Even");
    }
}

