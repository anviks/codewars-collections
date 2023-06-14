package me.anviks._6_kyu


/**
 * ## [Find The Parity Outlier](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)
 *
 * You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
 * array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
 * integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.
 *
 * ### Examples:
 * ```kotlin
 * [2, 4, 0, 100, 4, 11, 2602, 36] // Should return: 11 (the only odd number)
 * [160, 3, 1719, 19, 11, 13, -21] // Should return: 160 (the only even number)
 * ```
 */
fun find(integers: Array<Int>): Int {
    return if (integers.count { it % 2 == 0 } > 1) integers.find { it % 2 != 0 }!! else integers.find { it % 2 == 0 }!!
}

fun main() {
    println(find(arrayOf(2, 4, 0, 100, 4, 11, 2602, 36)))  // 11
    println(find(arrayOf(160, 3, 1719, 19, 11, 13, -21)))  // 160
    println(find(arrayOf(0, 1, 2)))  // 1
    println(find(arrayOf(1, 2, 3)))  // 2
    println(find(arrayOf(2, 6, 8, 10, 3)))  // 3
    println(find(arrayOf(0, 0, 3, 0, 0)))  // 3
    println(find(arrayOf(1, 1, 0, 1, 1)))  // 0
}
