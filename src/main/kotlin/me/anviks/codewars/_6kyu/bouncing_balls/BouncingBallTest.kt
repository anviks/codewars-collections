package me.anviks.codewars._6kyu.bouncing_balls

/*
 * https://www.codewars.com/kata/5544c7a5cb454edb3c000047
 */

import org.junit.Assert.*
import org.junit.Test

class BouncingBallTest {
    @Test
    fun test1() {
        assertEquals(3, bouncingBall(3.0, 0.66, 1.5))
    }

    @Test
    fun test2() {
        assertEquals(15, bouncingBall(30.0, 0.66, 1.5))
    }
}
