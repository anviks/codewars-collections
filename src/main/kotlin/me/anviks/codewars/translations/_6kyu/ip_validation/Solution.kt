/*
 * https://www.codewars.com/kata/515decfd9dcfc23bb6000006
 */

package me.anviks.codewars.translations._6kyu.ip_validation

fun isValidIp(string: String): Boolean =
    Regex("""^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$""")
        .matches(string)
