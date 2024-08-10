/*
 * https://www.codewars.com/kata/51fc12de24a9d8cb0e000001
 */

use regex::Regex;


pub fn valid_isbn10(isbn: &str) -> bool {
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

