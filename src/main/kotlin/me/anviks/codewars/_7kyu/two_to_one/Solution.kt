/*
 * https://www.codewars.com/kata/5656b6906de340bd1b0000ac
 */

package me.anviks.codewars._7kyu.two_to_one

fun longest(s1: String, s2: String): String {
    return s1.plus(s2).toSortedSet().joinToString("")
}