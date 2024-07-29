package me.anviks.codewars._6kyu.playing_with_passphrases

/*
 * https://www.codewars.com/kata/559536379512a64472000053
 */

object PlayPass {
    fun playPass(s: String, n: Int): String =
        s.map {
            if (it.isLetter()) ((it - 'A' + n) % 26 + 'A'.code).toChar()
            else if (it.isDigit()) (9 - it.digitToInt()).digitToChar()
            else it
        }.mapIndexed { index, c ->
            if (index % 2 == 1) c.lowercaseChar() else c
        }.joinToString("").reversed()
}
