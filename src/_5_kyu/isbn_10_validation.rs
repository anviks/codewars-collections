/*
 * https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
 */

use regex::Regex;


fn valid_isbn10(isbn: &str) -> bool {
    let pattern = r"^\d{9}(?:\d|X)$";
    let regex = Regex::new(pattern).unwrap();

    match regex.find(isbn) {
        None => return false,
        _ => ()
    }

    let sum = isbn.chars()
        .into_iter()
        .enumerate()
        .fold(0, |acc, (index, c)| acc + (index + 1) as u32 * c.to_digit(10).unwrap_or(10));

    sum % 11 == 0
}


// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::valid_isbn10;

    fn dotest(isbn: &str, expected: bool) {
        let actual = valid_isbn10(isbn);
        assert_eq!(actual, expected, "Test failed with isbn = {isbn}\nExpected {expected} but got {actual}")
    }
    
    #[test]
    fn sample_tests() {
        dotest("1112223339", true);
        dotest("048665088X", true);
        dotest("1293000000", true);
        dotest("1234554321", true);
        dotest("1234512345", false);
        dotest("1293", false);
        dotest("X123456788", false);
        dotest("ABCDEFGHIJ", false);
        dotest("XXXXXXXXXX", false);
        dotest("123456789T", false);
    }
}

