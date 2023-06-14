package me.anviks._7_kyu


/**
 * ## [Number of People in the Bus](https://www.codewars.com/kata/5648b12ce68d9daa6b000099)
 *
 * There is a bus moving in the city, and it takes and drops off some people at each bus stop.
 *
 * You are provided with a list (or array) of integer pairs. Each pair represents the number of people getting on the bus (the first item)
 * and the number of people getting off the bus (the second item) at a particular bus stop.
 *
 * Your task is to return the number of people who are still on the bus after the last bus stop (after the last pair in the array). Even though it is the last
 * bus stop, the bus is not empty, and some people are still on the bus, probably sleeping there. :D
 *
 * Take a look at the test cases.
 *
 * Please note that the test cases ensure that the number of people on the bus is always >= 0. So the returned integer cannot be negative.
 * The second value in the first pair of the array is 0 since the bus is empty at the first bus stop.
 */
fun people(busStops: Array<Pair<Int, Int>>) : Int {
    return busStops.sumOf { it.first - it.second }
}

fun main() {
    println(people(arrayOf(3 to 0, 9 to 1, 4 to 10, 12 to 2, 6 to 1, 7 to 10)))  // 17
}
