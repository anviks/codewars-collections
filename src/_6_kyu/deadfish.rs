/**
# [Deadfish](https://www.codewars.com/kata/51e0007c1f9378fa810002a9)

Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

- `i` increments the value (initially 0)
- `d` decrements the value
- `s` squares the value
- `o` outputs the value into the return array

Invalid characters should be ignored.

```rust
parse("iiisdoso") == vec![8, 64]
```
 */


fn parse(code: &str) -> Vec<i32> {
    let mut value: i32 = 0;
    let mut result_vec = vec![];

    for c in code.chars() {
        match c {
            'i' => value += 1,
            'd' => value -= 1,
            's' => value *= value,
            'o' => result_vec.push(value),
            _ => ()
        }
    }

    result_vec
}

pub fn main() {
    println!("{:?}", parse("iiisdoso"));  // [8, 64]
    println!("{:?}", parse("iiisdosodddddiso"));  // [8, 64, 3600]
}