/*
 * https://www.codewars.com/kata/55eeddff3f64c954c2000059
 */

package me.anviks.codewars.solutions._6kyu.sum_consecutives

import org.junit.Test
import kotlin.test.assertEquals

class ConsecutivesTest {

    @Test
    fun exampleTests() {
        assertEquals(listOf(1, 12, 0, 4, 6, 1), sumConsecutives(listOf(1, 4, 4, 4, 0, 4, 3, 3, 1)))
        assertEquals(listOf(2, 14, 3), sumConsecutives(listOf(1, 1, 7, 7, 3)))
        assertEquals(listOf(-10, 14, 12, 0), sumConsecutives(listOf(-5, -5, 7, 7, 12, 0)))
        assertEquals(listOf(12, 1), sumConsecutives(listOf(3, 3, 3, 3, 1)))
    }
}
