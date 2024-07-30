package me.anviks.codewars._6kyu.stop_gninnips_my_sdrow

/*
 * https://www.codewars.com/kata/5264d2b162488dc400000001
 */

fun spinWords(sentence: String): String =
    sentence.split(" ")
        .joinToString(" ")
        { if (it.length >= 5) it.reversed() else it }
