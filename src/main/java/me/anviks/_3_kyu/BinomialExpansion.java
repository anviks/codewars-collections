package me.anviks._3_kyu;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;


/**
 * <a href="https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b">Binomial Expansion</a>
 * <p>
 * The purpose of this kata is to write a program that can do some algebra.
 * </p>
 * <p>
 * Write a function <code>expand</code> that takes in an expresion with a single, one character variable, and expands it.
 * The expresion is in the form <code>(ax+b)^n</code> where <code>a</code> and <code>b</code> are integers which may be positive or negative,
 * <code>x</code> is any one character long variable, and <code>n</code> is a natural number. If <code>a = 1</code>, no coeficient will be placed in front of the variable.
 * If <code>a = -1</code>, a minus sign will be placed in front of the variable.
 * </p>
 * <p>
 * The expanded form should be returned as a string in the form <code>ax^b+cx^d+ex^f...</code> where <code>a</code>, <code>c</code>, and <code>e</code> are the coefficients of the term,
 * <code>x</code> is the original one character variable that was passed in the original expression and <code>b</code>, <code>d</code>, and <code>f</code>, are the powers that <code>x</code> is being raised to in each term and are in decreasing order.
 * </p>
 * <p>
 * If the coeficient of a term is zero, the term should not be included. If the coeficient of a term is one,
 * the coeficient should not be included. If the coeficient of a term is -1, only the minus sign should be included.
 * If the power of the term is 0, only the coeficient should be included. If the power of the term is 1, the carrot and power should be excluded.
 * </p>
 * <p>
 * <h3>Examples:</h3>
 * <pre>
 * <code>expand("(x+1)^2");</code>      // returns "x^2+2x+1"
 * <code>expand("(p-1)^3");</code>      // returns "p^3-3p^2+3p-1"
 * <code>expand("(2f+4)^6");</code>     // returns "64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096"
 * <code>expand("(-2a-4)^0");</code>    // returns "1"
 * <code>expand("(-12t+43)^2");</code>  // returns "144t^2-1032t+1849"
 * <code>expand("(r+0)^203");</code>    // returns "r^203"
 * <code>expand("(-x-1)^2");</code>     // returns "x^2+2x+1"
 * </pre>
 * </p>
 */
public class BinomialExpansion {
    public static String expand(String expr) {
        var arr = expr.split("\\^");
        int power = Integer.parseInt(arr[1]);
        if (power == 0) return "1";
        String operation = arr[0];

        Pattern pattern = Pattern.compile("(-?\\d*)([a-z])([+|-]\\d+)");
        Matcher matcher = pattern.matcher(operation);
        if (!matcher.find()) throw new RuntimeException("Input of '" + expr + "' has an incorrect pattern");

        String linearString = matcher.group(1);
        int linear;
        switch (linearString) {
            case "" -> linear = 1;
            case "-" -> linear = -1;
            default -> linear = Integer.parseInt(matcher.group(1));
        }

        char variable = matcher.group(2).charAt(0);
        int constant = Integer.parseInt(matcher.group(3));

        List<String> operands = new ArrayList<>();
        List<Integer> multipliers = getMultipliersFor(power);
        int splitter = 0;

        for (int multiplier : multipliers) {
            long tempPower = power - splitter;
            long tempLinear = (long) Math.pow(linear, tempPower);
            long tempConstant = (long) Math.pow(constant, splitter);

            String operand = "";
            operand += tempLinear * tempConstant * multiplier;

            // 3x^2+0x -> 3x^2
            if (operand.equals("0")) continue;

            // 1x -> x
            if (tempPower > 0) {
                if (operand.equals("1")) operand = "";
                else if (operand.equals("-1")) operand = "-";
                operand += variable;
            }

            if (tempPower > 1) {
                operand += "^" + tempPower;
            }

            operands.add(operand);
            splitter++;
        }

        StringBuilder builder = new StringBuilder();

        for (int i = 0; i < operands.size(); i++) {
            String operand = operands.get(i);

            if (operand.charAt(0) == '-') {
                operand = operand.substring(1);
                builder.append('-');
            } else if (i != 0) {
                builder.append('+');
            }

            builder.append(operand);
        }

        return builder.toString();
    }

    private static List<Integer> getMultipliersFor(int power) {
        // Get multipliers according to the binomial theorem
        List<Integer> multipliers = new ArrayList<>(List.of(1, 1));

        while (multipliers.size() <= power) {
            List<Integer> newMultipliers = new ArrayList<>();
            newMultipliers.add(1);
            for (int i = 0; i < multipliers.size() - 1; i++) {
                newMultipliers.add(multipliers.get(i) + multipliers.get(i + 1));
            }
            newMultipliers.add(1);
            multipliers = newMultipliers;
        }

        return multipliers;
    }

    static long binom(long N, long K) {
        long ret = 1;
        for (int k = 0; k < K; k++) {
            ret = ret * (N - k) / (k + 1);
        }
        return ret;
    }

    public static void main(String[] args) {
        System.out.println(expand("(4y+5)^3"));
//        System.out.println(binom(6, 3));
    }
}
