/*
 * https://www.codewars.com/kata/5264d2b162488dc400000001
 */

package me.anviks.codewars.solutions._6kyu.stop_gninnips_my_sdrow

import org.junit.Assert.assertEquals
import org.junit.Test

class SpinWordsTests {

    @Test
    fun test1() {
        assertEquals("emocleW", spinWords("Welcome"))
    }

    @Test
    fun test2() {
        assertEquals("Hey wollef sroirraw", spinWords("Hey fellow warriors"))
    }

    @Test
    fun test3() {
        assertEquals("This is a test", spinWords("This is a test"))
    }

    @Test
    fun test4() {
        assertEquals("This is rehtona test", spinWords("This is another test"))
    }

    @Test
    fun test5() {
        assertEquals("You are tsomla to the last test", spinWords("You are almost to the last test"))
    }

    @Test
    fun test6() {
        assertEquals("Just gniddik ereht is llits one more", spinWords("Just kidding there is still one more"))
    }
}
