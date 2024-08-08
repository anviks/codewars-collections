/*
 * https://www.codewars.com/kumite/66b146349574c9ea3dfafd0a?sel=66b146349574c9ea3dfafd0a
 */

package me.anviks.codewars.translations._5kyu.a_chain_adding_function

import kotlin.random.Random
import kotlin.test.Test
import kotlin.test.assertFalse
import kotlin.test.assertTrue

class SolutionTest {
    @Test
    fun basicTests() {
        assertTrue(add(1).equals(1), "add(1) should equal 1")
        assertTrue(add(1)(2).equals(3), "add(1)(2) should equal 3")
        assertTrue(add(1)(2)(3).equals(6), "add(1)(2)(3) should equal 6")
        assertTrue(add(1)(1)(1)(5)(28).equals(36), "add(1)(1)(1)(5)(28) should equal 36")

        assertFalse(add(1).equals(2), "add(1) should not equal 2")
        assertFalse(add(1)(2).equals(2), "add(1)(2) should not equal 2")
    }

    @Test
    fun shouldBeAbleToStoreValues() {
        val add4 = add(3)(1)
        val add7 = add(4)(3)
        add4(2)

        assertTrue(add4.equals(4), "should be able to store values")
        assertTrue(add7.equals(7), "should be able to store values")
    }

    @Test
    fun shouldBeAbleToContinueAdding() {
        val add5 = add(2)(3)
        val add9 = add(4)(5)
        assertTrue(add5(1).equals(6), "should be able to continue adding")
        assertFalse(add5(1).equals(9), "anti-cheat check")
        assertTrue(add9(5).equals(14), "should be able to continue adding")

        val add16 = add(7)(9)
        val add25 = add(12)(13)
        assertTrue(add16(1).equals(17), "should be able to continue adding")
        assertFalse(add16(1).equals(25), "anti-cheat check")
        assertTrue(add25(5).equals(30), "should be able to continue adding")
    }

    @Test
    fun shouldNotUseState() {
        val add5 = add(2)(3)
        val add14 = add5(4)(5)
        assertTrue(add5(8)(2).equals(15), "adding shouldn't mutate state")
        assertFalse(add5(8)(2).equals(14), "anti-cheat check")
        assertTrue(add14(2)(0)(3).equals(19), "adding shouldn't mutate state")

        val add16 = add(7)(9)
        val add25 = add16(9)
        assertTrue(add25(5).equals(30), "adding shouldn't mutate state")
        assertFalse(add25(5).equals(16), "anti-cheat check")
        assertTrue(add16(1).equals(17), "adding shouldn't mutate state")
    }

    @Test
    fun shouldBeAbleToAddInt() {
        val add5 = add(2)(3)
        val add20 = add(7)(9)(4)
        assertFalse(add5 + 5 == 5, "anti-cheat check")
        assertTrue(add5 + 5 == 10, "add(2)(3) + 5 should equal 10")
        assertTrue(add5 + 5 + 1 == 11, "add(2)(3) + 5 + 1 should equal 11")
        assertTrue(add20 + 1 == 21, "add(7)(9)(4) + 1 should equal 21")
        assertFalse(add20 + 1 == 20, "anti-cheat check")
    }

    @Test
    fun randomTests() {
        val random = Random.Default

        repeat(100) {
            val numbers = List(random.nextInt(1, 20)) { random.nextInt(1, 100) }
            val expected = numbers.sum()
            val actual = numbers.fold(add(0)) { acc, i -> acc(i) }
            assertTrue(actual.equals(expected), "Expected $actual to equal $expected")
            assertFalse(actual.equals(expected + random.nextInt(1, 20)), "anti-cheat check")
        }
    }
}