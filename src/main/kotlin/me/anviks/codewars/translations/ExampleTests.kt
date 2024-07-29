//package me.anviks.codewars.translations
//
//import org.junit.jupiter.api.Test
//import org.junit.jupiter.api.DisplayName
//import org.junit.jupiter.api.Assertions.assertEquals
//
//class SampleTests {
//    @Test
//    @DisplayName("Should return true for valid parentheses")
//    fun validCases() {
//        runTest(true, "()")
//        runTest(true, "((()))")
//        runTest(true, "()()()")
//        runTest(true, "(()())()")
//        runTest(true, "()(())((()))(())()")
//    }
//
//    @Test
//    @DisplayName("Should return false for invalid parentheses")
//    fun invalidCases() {
//        runTest(false, ")(")
//        runTest(false, "()()(")
//        runTest(false, "((())")
//        runTest(false, "())(()")
//        runTest(false, ")()")
//        runTest(false, ")")
//    }
//
//    @Test
//    @DisplayName("Should return true for empty strings")
//    fun emptyString() {
//        runTest(true, "")
//    }
//
//    private fun runTest(expected: Boolean, input: String) {
//        assertEquals(expected, validParentheses(input), "Test failed for input \"$input\"")
//    }
//}
//
