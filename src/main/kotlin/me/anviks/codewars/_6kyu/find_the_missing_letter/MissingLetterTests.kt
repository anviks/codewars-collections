/*
 * https://www.codewars.com/kata/5839edaa6754d6fec10000a2
 */

package me.anviks.codewars._6kyu.find_the_missing_letter

import org.junit.Test
import kotlin.test.assertEquals

class MissingLetterTests {

    @Test
    fun exampleTests() {
        assertEquals('e', findMissingLetter(charArrayOf('a', 'b', 'c', 'd', 'f')))
        assertEquals('P', findMissingLetter(charArrayOf('O', 'Q', 'R', 'S')))
    }
}
