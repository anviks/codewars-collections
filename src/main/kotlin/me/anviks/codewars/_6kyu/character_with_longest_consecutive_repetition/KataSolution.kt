/*
 * https://www.codewars.com/kata/586d6cefbcc21eed7a001155
 */

package me.anviks.codewars._6kyu.character_with_longest_consecutive_repetition

object KataSolution {
    fun longestRepetition(s: String): Pair<Char?,Int> {
        if (s.isEmpty()) return Pair(null, 0)
        var max = 1
        var count = 1
        var ch = s[0]
        for (i in 1 until s.length) {
            if (s[i] == s[i - 1]) {
                count++
                if (count > max) {
                    max = count
                    ch = s[i]
                }
            } else {
                count = 1
            }
        }
        return Pair(ch, max)
    }
}
