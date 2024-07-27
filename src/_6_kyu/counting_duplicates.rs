use std::collections::HashSet;
use std::ops::Add;
use std::str::Chars;

/**
# [Counting Duplicates](https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1)

Count the number of Duplicates

Write a function that will return the count of distinct case-insensitive alphabetic characters
and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

### Example
```rust
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
```
 */


fn count_duplicates(text: &str) -> u32 {
    let text = text.to_lowercase();
    let charset = text.chars().collect::<HashSet<_>>();
    charset.iter().filter(|c| text.chars().count() - text.replace(**c, "").len() > 1).count() as u32
}


pub fn main() {
    // println!("{}", count_duplicates("abcde"));  // 0
    // println!("{}", count_duplicates("aabbcde"));  // 2
    // println!("{}", count_duplicates("aabBcde"));  // 2
    // println!("{}", count_duplicates("indivisibility"));  // 1
    // println!("{}", count_duplicates("Indivisibilities"));  // 2
    // println!("{}", count_duplicates("aA11"));  // 2
    // println!("{}", count_duplicates("ABBA"));  // 2
}
