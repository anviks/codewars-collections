/*
 * https://www.codewars.com/kumite/66af6f1bb66160c4c3456f66?sel=66af6f1bb66160c4c3456f66
 */

package me.anviks.codewars.translations._6kyu.ip_validation

fun isValidIp(string: String): Boolean =
    Regex("""^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$""")
        .matches(string)
