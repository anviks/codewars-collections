package me.anviks.codewars.translations



fun validParentheses(parenStr: String): Boolean {
    var str = parenStr
    while (str.contains("()")) {
        str = str.replace("()", "")
    }
    return str.isEmpty()
}


fun main() {
    println(validParentheses("()"))  // true
    println(validParentheses("())"))  // false
    println(validParentheses(")(()))"))  // false
    println(validParentheses("("))  // false
    println(validParentheses("(())((()())())"))  // true
}
