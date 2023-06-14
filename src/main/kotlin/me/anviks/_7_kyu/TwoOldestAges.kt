package me.anviks._7_kyu


/**
 * ## [Two Oldest Ages](https://www.codewars.com/kata/511f11d355fe575d2c000001)
 *
 * The two oldest ages function/method needs to be completed. It should take an array of numbers as its argument and
 * return the two highest numbers within the array. The returned value should be an array in the format `[second oldest age, oldest age]`.
 *
 * The order of the numbers passed in could be any order. The array will always include at least 2 items.
 * If there are two or more of the oldest age, then return both of them in array format.
 *
 * For example:
 * ```kotlin
 * twoOldestAges(listOf(1, 2, 10, 8)) // should return listOf(8, 10)
 * twoOldestAges(listOf(1, 5, 87, 45, 8, 8)) // should return listOf(45, 87)
 * twoOldestAges(listOf(1, 3, 10, 0)) // should return listOf(3, 10)
 * ```
 */
fun twoOldestAges(ages: List<Int>): List<Int> {
    return ages.sortedDescending().subList(0, 2).sorted()
}

fun main() {
    println(twoOldestAges(listOf(1, 2, 10, 8)))  // should return listOf(8, 10)
    println(twoOldestAges(listOf(1, 5, 87, 45, 8, 8)))  // should return listOf(45, 87)
    println(twoOldestAges(listOf(1, 3, 10, 0)))  // should return listOf(3, 10)
    println(twoOldestAges(listOf(1, 3, 10, 0, 10)))  // should return listOf(10, 10)
    println(twoOldestAges(listOf(1, 3, 10, 0, 10, 10)))  // should return listOf(10, 10)
}
