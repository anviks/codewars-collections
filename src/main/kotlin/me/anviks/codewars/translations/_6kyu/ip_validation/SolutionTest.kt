/*
 * https://www.codewars.com/kata/515decfd9dcfc23bb6000006
 */

package me.anviks.codewars.translations._6kyu.ip_validation

import org.junit.Test
import kotlin.random.Random
import kotlin.test.assertEquals


class SolutionTest {
    @Test
    fun testCases() {
        assertEquals(true, isValidIp("0.0.0.0"))
        assertEquals(true, isValidIp("12.255.56.1"))
        assertEquals(true, isValidIp("137.255.156.100"))

        assertEquals(false, isValidIp(""))
        assertEquals(false, isValidIp("abc.def.ghi.jkl"))
        assertEquals(false, isValidIp("123.456.789.0"))
        assertEquals(false, isValidIp("12.34.56"))
        assertEquals(false, isValidIp("12.34.56.00"))
        assertEquals(false, isValidIp("12.34.56.7.8"))
        assertEquals(false, isValidIp("12.34.256.78"))
        assertEquals(false, isValidIp("1234.34.56"))
        assertEquals(false, isValidIp("pr12.34.56.78"))
        assertEquals(false, isValidIp("12.34.56.78sf"))
        assertEquals(false, isValidIp("12.34.56 .1"))
        assertEquals(false, isValidIp("12.34.56.-1"))
        assertEquals(false, isValidIp("123.045.067.089"))
    }

    @Test
    fun randomTests() {
        val letters = "abcdefghijklm"
        val rnd = Random.Default

        repeat(300) {
            val parts = mutableListOf<String>()
            repeat(4) { parts.add(rnd.nextInt(256).toString()) }

            val startIndex = rnd.nextInt(4)
            val someLetters = letters.substring(startIndex, startIndex + rnd.nextInt(1, 3))

            val pos = rnd.nextInt(4)
            var valid = false
            when (rnd.nextInt(12)) {
                0 -> valid = true
                1 -> parts[pos] = ""
                2 -> parts[pos] = someLetters
                3 -> parts[pos] = rnd.nextInt(256, 300).toString()
                4 -> parts.removeAt(pos)
                5 -> parts.add(rnd.nextInt(256).toString())
                6 -> parts[0] += someLetters
                7 -> parts[3] += someLetters
                8 -> parts[rnd.nextInt(1, 3)] += " "
                9 -> parts[pos] = "-" + parts[pos]
                10 -> parts[pos] = "0" + rnd.nextInt(0, 100)
                11 -> parts[pos] = "00"
            }

            val ip = parts.joinToString(".")
            assertEquals(valid, isValidIp(ip), "IP address: $ip")
        }
    }
}