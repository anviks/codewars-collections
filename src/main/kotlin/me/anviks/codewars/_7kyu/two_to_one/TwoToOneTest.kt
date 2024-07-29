package me.anviks.codewars._7kyu.two_to_one

/*
 * https://www.codewars.com/kata/5656b6906de340bd1b0000ac
 */

import org.junit.Assert.assertEquals
import org.junit.Test

class TwoToOneTest {
    @Test
    fun test() {
        println("longest Fixed Tests")
        assertEquals("aehrsty", longest("aretheyhere", "yestheyarehere"))
        assertEquals("abcdefghilnoprstu", longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
        assertEquals("acefghilmnoprstuy", longest("inmanylanguages", "theresapairoffunctions"))
    }
}
