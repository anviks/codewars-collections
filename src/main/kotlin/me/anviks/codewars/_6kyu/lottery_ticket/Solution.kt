/*
 * https://www.codewars.com/kata/57f625992f4d53c24200070e
 */

package me.anviks.codewars._6kyu.lottery_ticket

fun bingo(ticket: Array<Pair<String, Int>>, win: Int): String =
    if (ticket.count { pair -> pair.first.any { it.code == pair.second } } >= win) "Loser!"
    else "Winner!"
