/*
 * https://www.codewars.com/kata/5526fc09a1bbd946250002dc
 */

package me.anviks.codewars._6kyu.find_the_parity_outlier

fun find(integers: Array<Int>): Int {
    return if (integers.count { it % 2 == 0 } > 1) integers.find { it % 2 != 0 }!!
    else integers.find { it % 2 == 0 }!!
}
