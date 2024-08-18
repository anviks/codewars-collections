/*
 * https://www.codewars.com/kata/586d6cefbcc21eed7a001155
 */

package me.anviks.codewars.solutions._6kyu.character_with_longest_consecutive_repetition

import org.junit.Test
import kotlin.test.assertEquals

class SolutionTests {
    private fun runTest(s: String,sol: Pair<Char?,Int>) = assertEquals(sol,
        Solution.longestRepetition(
            s
        )
    )
    
    @Test fun `Example tests`() {
        runTest("aaaabb", Pair('a',4))
        runTest("bbbaaabaaaa", Pair('a',4))
        runTest("cbdeuuu900", Pair('u',3))
        runTest("abbbbb", Pair('b',5))
        runTest("aabb", Pair('a',2))
        runTest("", Pair(null,0))
        runTest("ba", Pair('b',1))
    }
}
