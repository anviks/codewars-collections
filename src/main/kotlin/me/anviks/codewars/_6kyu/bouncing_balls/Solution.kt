/*
 * https://www.codewars.com/kata/5544c7a5cb454edb3c000047
 */

package me.anviks.codewars._6kyu.bouncing_balls

fun bouncingBall(h: Double, bounce: Double, window: Double): Int {
    if (h <= 0 || bounce <= 0 || bounce >= 1 || window >= h) {
        return -1
    }

    var h2 = h
    var agg = -1

    while (h2 > window) {
        h2 *= bounce
        agg += 2
    }

    return agg
}
