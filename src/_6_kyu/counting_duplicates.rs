/*
 * https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 */

use std::collections::HashSet;


fn count_duplicates(text: &str) -> u32 {
    let text = text.to_lowercase();
    let charset = text.chars().collect::<HashSet<_>>();
    charset.iter().filter(|c| text.chars().count() - text.replace(**c, "").len() > 1).count() as u32
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_abcde() {
        assert_eq!(count_duplicates("abcde"), 0);
    }

    #[test]
    fn test_abcdea() {
        assert_eq!(count_duplicates("abcdea"), 1);
    }

    #[test]
    fn test_indivisibility() {
        assert_eq!(count_duplicates("indivisibility"), 1);
    }

    #[test]
    fn test_indivisibilities() {
        assert_eq!(count_duplicates("Indivisibilities"), 2);
    }

    #[test]
    fn test_aabbcde() {
        assert_eq!(count_duplicates("aabbcde"), 2);
        assert_eq!(count_duplicates("aabBcde"), 2);
    }
}

