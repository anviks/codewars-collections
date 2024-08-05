/*
 * https://www.codewars.com/kumite/66aff115efd8cb93759b1ccc?sel=66aff115efd8cb93759b1ccc
 */

package me.anviks.codewars.translations._6kyu.split_strings

fun solution(s: String): List<String> =
    s.chunked(2).map { it.padEnd(2, '_') }
