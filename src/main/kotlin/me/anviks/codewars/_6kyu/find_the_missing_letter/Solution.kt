/*
 * https://www.codewars.com/kata/5839edaa6754d6fec10000a2
 */

package me.anviks.codewars._6kyu.find_the_missing_letter

fun findMissingLetter(array: CharArray): Char {
    val alphabet = ('a'..'z').plus('A'..'Z')
    return alphabet.subList(alphabet.indexOf(array.first()), alphabet.indexOf(array.last())).subtract(array.toSet()).first()
}
