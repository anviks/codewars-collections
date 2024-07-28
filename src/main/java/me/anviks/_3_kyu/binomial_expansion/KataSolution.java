package me.anviks._3_kyu.binomial_expansion;

/*
 * https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
 */

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class KataSolution {
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
}
