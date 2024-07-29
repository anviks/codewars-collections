package me.anviks.codewars._7kyu.number_of_people_in_the_bus

/*
 * https://www.codewars.com/kata/5648b12ce68d9daa6b000099
 */

fun people(busStops: Array<Pair<Int, Int>>) : Int {
    return busStops.sumOf { it.first - it.second }
}
