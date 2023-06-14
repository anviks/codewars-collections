package me.anviks._7_kyu;

import java.util.Stack;


/**
 * <a href="https://www.codewars.com/kata/6411b91a5e71b915d237332d"><h2>Valid Parentheses</h2></a>
 * <p>
 * Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
 * The function should return true if the string is valid, and false if it's invalid.
 * </p>
 * <h3>Examples:</h3>
 * <pre>
 * <code>validParentheses( "()" ) => returns true</code>
 * <code>validParentheses( ")(()))" ) => returns false</code>
 * <code>validParentheses( "(" ) => returns false</code>
 * <code>validParentheses( "(())((()())())" ) => returns true</code>
 * </pre>
 * <h3>Constraints:</h3>
 * <pre>
 * <code>0 <= input.length <= 100</code>
 * </pre>
 * <ul>
 * <li>All inputs will be strings consisting only of parentheses <code>"()"</code></li>
 * <li>Empty strings are considered balanced (and therefore valid), and will be tested.</li>
 * <li>For languages with mutable strings, the inputs should not be mutated.</li>
 * </ul>
 */
public class ValidParentheses {
    public static boolean validParentheses(String parens) {
        Stack<String> parentheses = new Stack<>();
        for (String character : parens.split("")) {
            if (character.equals("(")) {
                parentheses.push("(");
            } else if (character.equals(")")) {
                if (parentheses.isEmpty()) {
                    return false;
                }
                parentheses.pop();
            }
        }

        return parentheses.isEmpty();
    }

    public static void main(String[] args) {
        System.out.println(validParentheses("()"));  // true
        System.out.println(validParentheses("())"));  // false
        System.out.println(validParentheses("("));  // false
        System.out.println(validParentheses("(())((()())())"));  // true
    }
}
