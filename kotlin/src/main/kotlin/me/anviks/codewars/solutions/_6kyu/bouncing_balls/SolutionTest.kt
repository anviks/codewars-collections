/*
 * https://www.codewars.com/kata/5544c7a5cb454edb3c000047
 */

package me.anviks.codewars.solutions._6kyu.bouncing_balls

import org.junit.Assert.*
import org.junit.Test

class SolutionTest {
    @Test
    fun test1() {
        assertEquals(3, me.anviks.codewars.solutions._6kyu.bouncing_balls.bouncingBall(3.0, 0.66, 1.5))
    }

    @Test
    fun test2() {
        assertEquals(15, me.anviks.codewars.solutions._6kyu.bouncing_balls.bouncingBall(30.0, 0.66, 1.5))
    }
}
