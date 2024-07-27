/**
# [Find the missing term in an Arithmetic Progression](https://www.codewars.com/kata/52de553ebb55d1fca3000371)

An Arithmetic Progression is defined as one in which there is a constant difference between the consecutive terms of a given series of numbers.
You are provided with consecutive elements of an Arithmetic Progression. There is however one hitch: exactly one term from the original series is missing from the set of numbers which have been given to you.
The rest of the given series is the same as the original AP. Find the missing term.

You have to write the function findMissing(list), list will always be at least 3 numbers. The missing term will never be the first or last one.

## Example:
```rust
find_missing(&[1, 3, 5, 9, 11]) == 7
```

PS: This is a sample question of the facebook engineer challenge on interviewstreet.
I found it quite fun to solve on paper using math, derive the algo that way.
Have fun!
*/

use std::cmp::{max, min};
use std::collections::HashSet;
use std::ops::Sub;

fn find_missing(seq: &[i32]) -> i32 {
    let (first, last) = (*seq.first().unwrap(), *seq.last().unwrap());
    let (min, max) = (min(first, last), max(first, last));
    let d: HashSet<i32> = (min..max + 1).step_by(((max - min) as usize / seq.len()) as usize).collect();

    *d.sub(&seq.iter().cloned().collect::<HashSet<i32>>()).iter().last().unwrap()
}

pub fn main() {
    println!("{}", find_missing(&[1, 2, 3, 4, 6, 7, 8, 9]));  // 5
    println!("{}", find_missing(&[1, 3, 4, 5, 6, 7, 8, 9]));  // 2
    println!("{}", find_missing(&[1, 3, 5, 9, 11]));  // 7
}
