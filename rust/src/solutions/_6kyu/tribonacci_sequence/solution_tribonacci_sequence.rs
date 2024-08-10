/*
 * https://www.codewars.com/kata/556deca17c58da83c00002db
 */

pub fn tribonacci(signature: &[f64; 3], n: usize) -> Vec<f64> {
    let mut vec: Vec<f64> = Vec::with_capacity(n);
    vec.extend_from_slice(
        if n < 3 { &signature[..n] } else { signature }
    );

    while vec.len() < n {
        vec.push((vec[vec.len() - 3..]).iter().sum())
    }

    vec
}
