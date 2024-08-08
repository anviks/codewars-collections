/*
 * https://www.codewars.com/kata/55466989aeecab5aac00003e
 */

package me.anviks.codewars.solutions._6kyu.rectangle_into_squares

fun sqInRect(lng: Int, wdth: Int): List<Int>? {
    return if (lng == wdth) null
    else recursiveSqInRect(lng, wdth)
}

private fun recursiveSqInRect(lng: Int, wdth: Int): List<Int> {
    return if (lng * wdth != 0) {
        val size = listOf(lng, wdth).sorted().toMutableList()
        size[1] -= size[0]
        recursiveSqInRect(size[0], size[1]).plus(size[0]).sortedDescending()
    } else {
        mutableListOf()
    }
}
