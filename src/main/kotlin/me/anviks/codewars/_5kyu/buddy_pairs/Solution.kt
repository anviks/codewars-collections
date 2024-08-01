package me.anviks.codewars._5kyu.buddy_pairs

/*
 * https://www.codewars.com/kata/59ccf051dcc4050f7800008f
 */

import kotlin.math.sqrt

private fun getSumOfDivisors(n: Long): Long {
    var divisorSum = 1L
    for (m in 2L..sqrt(n.toDouble()).toLong()) {
        if (n % m == 0L) {
            divisorSum += m
            divisorSum += if (n / m != m) n / m else 0
        }
    }
    return divisorSum
}

fun buddy(start: Long, limit: Long): String {
    for (n in start..limit) {
        val nDivSum = getSumOfDivisors(n)
        val m = nDivSum - 1
        val mDivSum = getSumOfDivisors(m)

        if (m > n && mDivSum == n + 1) {
            return "($n $m)"
        }
    }

    return "Nothing"
}
