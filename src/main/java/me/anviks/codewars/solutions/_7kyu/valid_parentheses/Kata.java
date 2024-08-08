/*
 * https://www.codewars.com/kata/6411b91a5e71b915d237332d
 */

package me.anviks.codewars.solutions._7kyu.valid_parentheses;

import java.util.Stack;

public class Kata {
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
}
