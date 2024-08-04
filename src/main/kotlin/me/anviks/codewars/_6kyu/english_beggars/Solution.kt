/*
 * https://www.codewars.com/kata/59590976838112bfea0000fa
 */

package me.anviks.codewars._6kyu.english_beggars

fun beggars(values: List<Int>, n: Int): List<Int> =
    (0..<n).map { values.slice(it..<values.size step n).sum() }
