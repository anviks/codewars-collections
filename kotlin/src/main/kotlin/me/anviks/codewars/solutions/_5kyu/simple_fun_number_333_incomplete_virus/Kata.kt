/*
 * https://www.codewars.com/kata/595467c63074e38ba4000063
 */

package me.anviks.codewars.solutions._5kyu.simple_fun_number_333_incomplete_virus


object Kata {
    fun incompleteVirus(s: String): Long {
        var binaryString = ""
        var largeDigitEncountered = false

        for (char in s) {
            if (!largeDigitEncountered && char < '2') {
                binaryString += char
            } else {
                largeDigitEncountered = true
                binaryString += '1'
            }
        }

        return binaryString.toLong(2)
    }
}

