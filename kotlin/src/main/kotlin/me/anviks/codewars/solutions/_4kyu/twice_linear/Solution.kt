/*
 * https://www.codewars.com/kata/5672682212c8ecf83e000050
 */

package me.anviks.codewars.solutions._4kyu.twice_linear

import java.util.*

fun next(x: Int): Pair<Int, Int> = Pair(2 * x + 1, 3 * x + 1)

fun dblLinear(n: Int): Int {
    val result = mutableSetOf<Int>()
    val queue: Queue<Int> = PriorityQueue()
    queue.add(1)

    while (result.size <= n) {
        val queueHead = queue.remove()
        result.add(queueHead)

        val nextNumbers = next(queueHead)

        queue.add(nextNumbers.first)
        queue.add(nextNumbers.second)
    }

    return result.last()
}
