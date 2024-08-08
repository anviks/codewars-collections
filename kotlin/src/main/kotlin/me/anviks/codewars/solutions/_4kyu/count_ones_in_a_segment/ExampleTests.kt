/*
 * https://www.codewars.com/kata/596d34df24a04ee1e3000a25
 */

package me.anviks.codewars.solutions._4kyu.count_ones_in_a_segment

import org.junit.Test
import kotlin.test.assertEquals

class ExampleTests {
    private fun runTest(left: Long, right: Long, sol: Long) = assertEquals(sol,
        Kata.countOnes(left, right)
    )

    @Test
    fun `Sample tests`() {
        runTest(4, 7, 8)
        runTest(5, 7, 7)
        runTest(12, 29, 51)
        runTest(107987542948666, 121359343536179, 321522960003023)
    }
}
