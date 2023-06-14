package me.anviks._6_kyu


/**
 * ## [Rectangle into Squares](https://www.codewars.com/kata/55466989aeecab5aac00003e)
 *
 * The drawing below gives an idea of how to cut a given "true" rectangle into squares ("true" rectangle meaning that
 * the two dimensions are different).
 *
 * [Rectangle into Squares](https://i.imgur.com/lk5vJ7sm.jpg)
 *
 * Can you translate this drawing into an algorithm?
 *
 * You will be given two dimensions
 * 1. a positive integer length (parameter named `lng`)
 * 2. a positive integer width (parameter named `wdth`)
 *
 * You will return an array or a string (depending on the language; Shell bash and Fortran return a string) with the
 * size of each of the squares.
 *
 * ### Examples in general form:
 * ```kotlin
 * sqInRect(5, 3) should return arrayListOf(3, 2, 1, 1)
 * sqInRect(3, 5) should return arrayListOf(3, 2, 1, 1)
 * ```
 *
 * ### Notes:
 * - `lng == wdth` as a starting case would be an entirely different problem and the drawing is planned to be interpreted
 * with `lng != wdth`. (See kata, Square into Squares. Protect trees! http://www.codewars.com/kata/54eb33e5bc1a25440d000891
 * for this problem).
 * - When the initial parameters are so that `lng` == `wdth`, the solution `[lng]` would be the most obvious but not in
 * the spirit of this kata so, in that case, return `null`.
 */
fun sqInRect(lng: Int, wdth: Int): List<Int>? {
    return if (lng == wdth) null
    else recursiveSqInRect(lng, wdth)
}

private fun recursiveSqInRect(lng: Int, wdth: Int): List<Int> {
    return if (lng * wdth != 0) {
        var idk = ArrayList<Int>(listOf(lng, wdth))
        val size = listOf(lng, wdth).sorted().toMutableList()
        size[1] -= size[0]
        recursiveSqInRect(size[0], size[1]).plus(size[0]).sortedDescending()
    } else {
        mutableListOf()
    }
}

fun main() {
    println(sqInRect(5, 3))  // [3, 2, 1, 1]
    println(sqInRect(5, 5))  // null
    println(sqInRect(20, 14))  // [14, 6, 6, 2, 2, 2]
    println(sqInRect(240, 32))  // [32, 32, 32, 32, 32, 32, 32, 16, 16]
}
