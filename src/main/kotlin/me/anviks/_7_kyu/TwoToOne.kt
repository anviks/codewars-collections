package me.anviks._7_kyu


/**
 * ## [Two to One](https://www.codewars.com/kata/5656b6906de340bd1b0000ac)
 *
 * Take 2 strings `s1` and `s2` including only letters from `a` to `z`. Return a new sorted string, the longest possible,
 * containing distinct letters - each taken only once - coming from `s1` or `s2`.
 *
 * <br/><br/>
 * ### Examples:
 * ```kotlin
 * a = "xyaabbbccccdefww"
 * b = "xxxxyyyyabklmopq"
 * longest(a, b) -> "abcdefklmopqwxy"
 *
 * a = "abcdefghijklmnopqrstuvwxyz"
 * longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
 * ```
 */
fun longest(s1: String, s2: String): String {
    return s1.plus(s2).toSortedSet().joinToString("")
}

fun main() {
    println(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))  // abcdefklmopqwxy
    println(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))  // abcdefghijklmnopqrstuvwxyz
}
