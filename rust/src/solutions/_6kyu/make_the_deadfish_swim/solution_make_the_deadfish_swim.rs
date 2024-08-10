/*
 * https://www.codewars.com/kata/51e0007c1f9378fa810002a9
 */

pub fn parse(code: &str) -> Vec<i32> {
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
