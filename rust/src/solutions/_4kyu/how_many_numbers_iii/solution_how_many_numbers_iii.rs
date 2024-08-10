/*
 * https://www.codewars.com/kata/5877e7d568909e5ff90017e6
 */


use std::ops::Add;

pub fn find_all(sum_dig: u8, digs: u8) -> Option<(usize, u64, u64)> {
    let nums: Vec<Vec<u8>> = get_ascending_digits(digs, 1).into_iter()
        .filter(
            |vec| vec.iter().sum::<u8>() == sum_dig
        ).collect();

    return match nums.len() {
        0 => None,
        _ => Some((nums.len(), digit_vec_to_num(nums.first().unwrap()), digit_vec_to_num(nums.last().unwrap())))
    };
}

fn digit_vec_to_num(digits: &Vec<u8>) -> u64 {
    digits.iter().fold(String::new(), |acc, d| acc.add(&*d.to_string())).parse().unwrap()
}

fn get_ascending_digits(digs: u8, minimum: u8) -> Vec<Vec<u8>> {
    let mut result = vec![];

    if digs == 1 {
        for x in minimum..10 {
            result.push(vec![x]);
        }
    } else {
        for x in minimum..10 {
            let vec1 = vec![x];
            for mut y in get_ascending_digits(digs - 1, x) {
                let mut vecc = vec1.clone();
                vecc.append(&mut y);
                result.push(vecc)
            }
        }
    }

    result
}

