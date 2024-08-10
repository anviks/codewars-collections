/*
 * https://www.codewars.com/kata/55b195a69a6cc409ba000053
 */

use std::collections::HashSet;

fn generate_inc(digits: u32, start: u8) -> Vec<Vec<u8>> {
    let mut increasing_nums = vec![];

    if digits <= 1 {
        for i in start..10 {
            increasing_nums.push(vec![i]);
        }
    } else {
        for j in start..10 {
            for mut i in generate_inc(digits - 1, j) {
                i.insert(0, j);
                increasing_nums.push(i);
            }
        }
    }

    increasing_nums
}

fn generate_dec(digits: u32, end: u8) -> Vec<Vec<u8>> {
    let mut decreasing_nums = vec![];

    if digits <= 1 {
        for i in 0..=end {
            decreasing_nums.push(vec![i]);
        }
    } else {
        for j in 0..=end {
            for mut i in generate_dec(digits - 1, j) {
                i.insert(0, j);
                decreasing_nums.push(i);
            }
        }
    }

    decreasing_nums
}

pub fn total_inc_dec(n: u32) -> u64 {
    if n == 0 { return 1; }

    let mut inc_dec = vec![];

    for i in 0..=n {
        inc_dec.append(&mut generate_inc(i, 1));
        inc_dec.append(&mut generate_dec(i, 9));
    }

    let distinct = inc_dec.into_iter()
        .filter(|v| v.len() == 1 || v.iter().sum::<u8>() != 0)  // remove [0, 0], [0, 0, 0] and so on
        .collect::<HashSet<Vec<u8>>>();

    distinct.len() as u64
}