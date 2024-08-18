/*
 * https://www.codewars.com/kata/559536379512a64472000053
 */

package me.anviks.codewars.solutions._6kyu.playing_with_passphrases

import org.junit.Test
import kotlin.test.assertEquals

class SolutionTest {

    @Test
    fun basicTests() {
        assertEquals("!!!VpZ FwPm j ", Solution.playPass(" I LOVE YOU!!!", 1))
        assertEquals("!!!uOy eVoL I", Solution.playPass("I LOVE YOU!!!", 0))
        assertEquals("zDdCcBbB", Solution.playPass("AAABBCCY", 1))
    }
}
