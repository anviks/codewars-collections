/*
 * https://www.codewars.com/kata/52de553ebb55d1fca3000371
 */

use std::cmp::{max, min};
use std::collections::HashSet;
use std::ops::Sub;

pub fn find_missing(seq: &[i32]) -> i32 {
    let (first, last) = (*seq.first().unwrap(), *seq.last().unwrap());
    let (min, max) = (min(first, last), max(first, last));
    let d: HashSet<i32> = (min..max + 1).step_by((max - min) as usize / seq.len()).collect();

    *d.sub(&seq.iter().cloned().collect::<HashSet<i32>>()).iter().last().unwrap()
}
