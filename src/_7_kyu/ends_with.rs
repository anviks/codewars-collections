/**
# [Ends with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d)

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

## Examples:

```rust
solution('abc', 'bc') // returns true
solution('abc', 'd') // returns false
```
 */


fn solution(word: &str, ending: &str) -> bool {
    word.ends_with(ending)
}

pub fn main() {
    println!("{}", solution("abc", "c"));  // true
    println!("{}", solution("abc", "bc"));  // true
    println!("{}", solution("abc", "d"));  // false
}