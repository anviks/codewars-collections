/*
 * https://www.codewars.com/kumite/66ae6d495b5b458eac8b2811?sel=66ae6d495b5b458eac8b2811
 */

package me.anviks.codewars.forks._6kyu.lottery_ticket

fun bingo(ticket: Array<Pair<String, Int>>, win: Int): String {
    val sum = ticket.fold(0) { a, (str, num) -> a + if (str.any { s -> s.code == num }) 1 else 0 }
    return if (sum >= win) "Winner!" else "Loser!"
}
