package codewars

import kotlin.math.min

fun longest(s1: String, s2: String): String {
    return s1.plus(s2).toSortedSet().joinToString("")
}

fun twoOldestAges(ages: List<Int>): List<Int> {
    return ages.sortedDescending().subList(0, 2).sorted()
}

fun find(integers: Array<Int>): Int {
    return if (integers.count { it % 2 == 0 } > 1) integers.find { it % 2 != 0 }!! else integers.find { it % 2 == 0 }!!
}

fun findMissingLetter(array: CharArray): Char {
    val alphabet = ('a'..'z').plus('A'..'Z')
    return alphabet.subList(alphabet.indexOf(array.first()), alphabet.indexOf(array.last())).subtract(array.toSet())
        .first()
}

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


fun main() {
    println(sqInRect(5, 3))
    println(sqInRect(5, 5))
}
