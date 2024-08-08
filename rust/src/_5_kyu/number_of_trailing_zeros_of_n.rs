/*
 * https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
 */


fn zeros(n: u64) -> u64 {
    let r = n / 5;
    if r >= 5 { return zeros(r) + r; }
    return r;
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sample_tests() {
        assert_eq!(zeros(0), 0);
        assert_eq!(zeros(6), 1);
        assert_eq!(zeros(14), 2);
        assert_eq!(zeros(30), 7);
        assert_eq!(zeros(1000), 249);
        assert_eq!(zeros(100000), 24999);
        assert_eq!(zeros(1000000000), 249999998);
    }
}
