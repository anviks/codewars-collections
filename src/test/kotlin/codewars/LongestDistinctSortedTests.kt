package codewars

import me.anviks.codewars.longest
import org.junit.Assert.assertEquals
import org.junit.Test

class LongestDistinctSortedTests {
    @Test
    fun test() {
        assertEquals("aehrsty", longest("aretheyhere", "yestheyarehere"))
        assertEquals("abcdefghilnoprstu", longest("loopingisfunbutdangerous", "lessdangerousthancoding"))
        assertEquals("acefghilmnoprstuy", longest("inmanylanguages", "theresapairoffunctions"))
    }
}