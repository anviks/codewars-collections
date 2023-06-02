package org.anviks;

import java.util.ArrayList;

public class ValidParentheses {
    public static boolean validParentheses(String parens) {
        ArrayList<String> parentheses = new ArrayList<>();

        for (String character : parens.split("")) {
            if (character.equals("(")) {
                parentheses.add("(");
            } else if (character.equals(")")) {
                if (!parentheses.remove("(")) {
                    return false;
                }
            }
        }

        return parentheses.isEmpty();
    }
}
