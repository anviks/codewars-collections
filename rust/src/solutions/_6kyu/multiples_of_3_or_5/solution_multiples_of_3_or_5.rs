/*
 * https://www.codewars.com/kata/514b92a657cdc65150000006
 */

pub fn solution(num: i32) -> i32 {
    (1..num).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}
