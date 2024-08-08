/*
 * https://www.codewars.com/kata/596d34df24a04ee1e3000a25
 */

package me.anviks.codewars.solutions._4kyu.count_ones_in_a_segment

import kotlin.math.floor
import kotlin.math.log2
import kotlin.math.pow


object Kata {
    private fun numberOfOnes(x: Long): Long {
        var result = 0L
        var current = x

        while (current > 0) {
            val p = floor(log2(current.toDouble())).toInt()
            val a = p * 2.0.pow(p - 1).toLong()
            val c = current - 2.0.pow(p).toLong() + 1

            result += a + c
            current -= 2.0.pow(p).toLong()
        }

        return result
    }

    fun countOnes(left: Long, right: Long): Long {
        return numberOfOnes(right) - numberOfOnes(
            left - 1
        )
    }
}
