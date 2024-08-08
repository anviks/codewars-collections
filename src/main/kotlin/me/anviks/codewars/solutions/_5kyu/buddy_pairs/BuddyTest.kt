/*
 * https://www.codewars.com/kata/59ccf051dcc4050f7800008f
 */

package me.anviks.codewars.solutions._5kyu.buddy_pairs

import org.junit.Test
import kotlin.test.assertEquals

class BuddyTest {

    @Test
    fun exampleTests() {
        testing(1071625, 1103735, "(1081184 1331967)")
        testing(2382, 3679, "Nothing")
        testing(381, 4318, "(1050 1925)")
    }

    private fun testing(start: Long, limit: Long, expected: String) {
        println("Start: $start, Limit: $limit, Expected: $expected")
        assertEquals(expected, buddy(start, limit))
    }
}
