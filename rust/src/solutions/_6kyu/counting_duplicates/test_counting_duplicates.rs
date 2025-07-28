/*
 * https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1
 */

#[cfg(test)]
mod tests {
    use super::super::solution_counting_duplicates::*;

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
}

