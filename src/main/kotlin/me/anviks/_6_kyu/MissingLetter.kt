package me.anviks._6_kyu


/**
 * ## [Find the missing letter](https://www.codewars.com/kata/5839edaa6754d6fec10000a2)
 *
 * Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
 * in the array.
 *
 * You will always get a valid array. And it will be always exactly one letter be missing. The length of the array will
 * always be at least 2.
 * The array will always contain letters in only one case.
 *
 * ### Example:
 * ```kotlin
 * ['a','b','c','d','f'] -> 'e'
 * ['O','Q','R','S'] -> 'P'
 * ```
 * (Use the English alphabet with 26 letters!)
 *
 * Have fun coding it and please don't forget to vote and rank this kata! :-)
 *
 * I have also created other katas. Take a look if you enjoyed this kata!
 */
fun findMissingLetter(array: CharArray): Char {
    val alphabet = ('a'..'z').plus('A'..'Z')
    return alphabet.subList(alphabet.indexOf(array.first()), alphabet.indexOf(array.last())).subtract(array.toSet()).first()
}

fun main() {
    println(findMissingLetter(charArrayOf('a', 'b', 'c', 'd', 'f')))  // 'e'
    println(findMissingLetter(charArrayOf('O', 'Q', 'R', 'S')))  // 'P'
}
