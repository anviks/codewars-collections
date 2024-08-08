/*
 * https://www.codewars.com/kata/52de553ebb55d1fca3000371
 */

use std::cmp::{max, min};
use std::collections::HashSet;
use std::ops::Sub;

fn find_missing(seq: &[i32]) -> i32 {
    let (first, last) = (*seq.first().unwrap(), *seq.last().unwrap());
    let (min, max) = (min(first, last), max(first, last));
    let d: HashSet<i32> = (min..max + 1).step_by(((max - min) as usize / seq.len())).collect();

    *d.sub(&seq.iter().cloned().collect::<HashSet<i32>>()).iter().last().unwrap()
}


// Add your tests here.
// See https://doc.rust-lang.org/stable/rust-by-example/testing/unit_testing.html

#[cfg(test)]
mod tests {
    use super::find_missing;
    
    const ERR_MSG: &str = "\nYour result (left) did not match the expected output (right)";
    
    fn dotest(a: &[i32], expected: i32) {
        assert_eq!(find_missing(a), expected, "{ERR_MSG} with seq = {a:?}")
    }

    #[test]
    fn fixed_tests() {
        dotest(&[1, 2, 3, 4, 6, 7, 8, 9], 5);
        dotest(&[1, 3, 4, 5, 6, 7, 8, 9], 2);
        dotest(&[1, 3, 5, 9, 11], 7);
    }
}

