/*
 * https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d
 */


fn solution(word: &str, ending: &str) -> bool {
  word.ends_with(ending)
}


// Rust test example:
// See: https://doc.rust-lang.org/book/testing.html

#[test]
fn returns_expected() {
  assert_eq!(true, solution("abc", "c"));
  assert_eq!(false, solution("strawberry", "banana"));
}
