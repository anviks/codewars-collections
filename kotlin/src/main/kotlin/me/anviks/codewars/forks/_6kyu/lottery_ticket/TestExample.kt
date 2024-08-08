/*
 * https://www.codewars.com/kumite/66ae6d495b5b458eac8b2811?sel=66ae6d495b5b458eac8b2811
 */

package me.anviks.codewars.forks._6kyu.lottery_ticket

import kotlin.test.assertEquals
import org.junit.Test

class TestExample {
    private fun _bingo(ticket: Array<Pair<String, Int>>, win: Int): String {
        val sum = ticket.fold(0) { a, (str, num) -> a + if (str.any { s -> s.code == num }) 1 else 0 }
        return if (sum >= win) "Winner!" else "Loser!"
    }

    private fun rand(from: Int, to: Int): Int {
        return Math.floor((to - from + 1) * Math.random() + from).toInt()
    }

    private val names = arrayOf(
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z"
    )
    private val nums =
        arrayOf(65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90)

    private fun generateString(): String = Array(rand(2, 8)) { names[rand(0, 25)] }.joinToString("")

    @Test
    fun `Basic tests`() {
        assertEquals("Loser!", bingo(arrayOf("ABC" to 65, "HGR" to 74, "BYHT" to 74), 2))
        assertEquals("Winner!", bingo(arrayOf("ABC" to 65, "HGR" to 74, "BYHT" to 74), 1))
        assertEquals("Loser!", bingo(arrayOf("HGTYRE" to 74, "BE" to 66, "JKTY" to 74), 3))
    }

    @Test
    fun `Random tests`() {
        for (i in 1..100) {
            val len = rand(2, 10)
            val win = rand(1, len)
            val ticket = Array(len) {
                generateString() to nums[rand(0, 25)]
            }
            assertEquals(_bingo(ticket, win), bingo(ticket, win))
        }
    }
}