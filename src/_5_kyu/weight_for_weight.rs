/*
 * https://www.codewars.com/kata/55c6126177c9441a570000cc
 */

fn order_weight(s: &str) -> String {
    let nums_str: Vec<&str> = s.split(" ").collect();
    let nums: Vec<u32> = nums_str.iter()
        .map(|&s| s.chars()
            .fold(0, |acc, c| acc + c.to_digit(10).unwrap_or(0)))
        .collect();

    let mut combined: Vec<(&str, u32)> = nums_str.into_iter().zip(nums).collect();
    combined.sort_by_key(|&tuple| (tuple.1, tuple.0));
    let (nums_str, _): (Vec<&str>, Vec<u32>) = combined.into_iter().unzip();

    nums_str.join(" ")
}

fn testing(s: &str, exp: &str) -> () {
    assert_eq!(order_weight(s), exp)
}

#[test]
fn basics_order_weight() {
    testing("103 123 4444 99 2000", "2000 103 123 4444 99");
    testing("2000 10003 1234000 44444444 9999 11 11 22 123", 
        "11 11 2000 10003 22 123 1234000 44444444 9999");
}