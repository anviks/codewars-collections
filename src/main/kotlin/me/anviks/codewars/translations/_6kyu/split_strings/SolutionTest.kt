package me.anviks.codewars.translations._6kyu.split_strings

import kotlin.random.Random
import kotlin.test.Test
import kotlin.test.assertEquals


class SolutionTest {
    @Test
    fun basicTests() {
        assertEquals(listOf(), solution(""), "Should handle empty string")
        assertEquals(listOf("ab", "cd", "ef"), solution("abcdef"), "Should handle even string")
        assertEquals(listOf("ab", "cd", "ef", "g_"), solution("abcdefg"), "Should handle odd string")
    }

    @Test
    fun spacesTests() {
        assertEquals(listOf("H ", " e", "l ", " l", "o_"), solution("H  el  lo"), "Should handle spaces")
        assertEquals(listOf("w ", "  ", "o ", " r", "l ", "d_"), solution("w   o  rl d"), "Should handle spaces")
    }

    @Test
    fun randomTests() {
        val random = Random.Default
        val chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ       1234567890______"

        repeat(300) {
            val parts = mutableListOf<String>()
            repeat(random.nextInt(1, 10)) {
                parts.add(chars[random.nextInt(chars.length)].toString())
            }
            val str = parts.joinToString("")
            val expected = str.chunked(2).map { it.padEnd(2, '_') }
            assertEquals(expected, solution(str), "Failed with input: $str")
        }
    }
}