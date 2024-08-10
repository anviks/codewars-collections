/*
 * https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 */

use std::collections::HashSet;

pub fn count_duplicates(text: &str) -> u32 {
    let text = text.to_lowercase();
    let charset = text.chars().collect::<HashSet<_>>();
    charset.iter().filter(|c| text.chars().count() - text.replace(**c, "").len() > 1).count() as u32
}

