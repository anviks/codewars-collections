/*
 * https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
 */

pub fn zeros(n: u64) -> u64 {
    let r = n / 5;
    if r >= 5 { return zeros(r) + r; }
    return r;
}
