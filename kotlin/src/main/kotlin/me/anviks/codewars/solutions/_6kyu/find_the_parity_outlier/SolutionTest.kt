/*
 * https://www.codewars.com/kata/5526fc09a1bbd946250002dc
 */

package me.anviks.codewars.solutions._6kyu.find_the_parity_outlier

import kotlin.test.assertEquals
import org.junit.Test

class SolutionTest {
    @Test
    fun testExample() {
        val exampleTest1 = arrayOf(2, 6, 8, -10, 3)
        val exampleTest2 = arrayOf(206847684, 1056521, 7, 17, 1901, 21104421, 7, 1, 35521, 1, 7781)
        val exampleTest3 = arrayOf(Integer.MAX_VALUE, 0, 1)
        assertEquals(3, find(exampleTest1))
        assertEquals(206847684, find(exampleTest2))
        assertEquals(0, find(exampleTest3))
    }
}
