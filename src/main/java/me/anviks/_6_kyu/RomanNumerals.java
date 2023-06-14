package me.anviks._6_kyu;

import java.util.ArrayList;
import java.util.Arrays;


/**
 * <a href="https://www.codewars.com/kata/51b62bf6a9c58071c600001b"><h2>Roman Numerals Encoder</h2></a>
 * <p>
 * Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral
 * representation of that integer.
 * </p>
 * <p>
 * Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
 * any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
 * 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
 * </p>
 * <p>
 * Example:
 * </p>
 * <pre>
 * <code>conversion.solution(1000); // should return "M"</code>
 * <code>conversion.solution(1990); // should return "MCMXC"</code>
 * <code>conversion.solution(2007); // should return "MMVII"</code>
 * </pre>
 */
public class RomanNumerals {

    public static String toRoman(int n) {
        StringBuilder b = new StringBuilder();
        b.append("M".repeat(n / 1000));
        n %= 1000;
        b.append("CM".repeat(n / 900));
        n %= 900;
        b.append("D".repeat(n / 500));
        n %= 500;
        b.append("CD".repeat(n / 400));
        n %= 400;
        b.append("C".repeat(n / 100));
        n %= 100;
        b.append("XC".repeat(n / 90));
        n %= 90;
        b.append("L".repeat(n / 50));
        n %= 50;
        b.append("XL".repeat(n / 40));
        n %= 40;
        b.append("X".repeat(n / 10));
        n %= 10;
        b.append("IX".repeat(n / 9));
        n %= 9;
        b.append("V".repeat(n / 5));
        n %= 5;
        b.append("IV".repeat(n / 4));
        n %= 4;
        b.append("I".repeat(n));

        return b.toString();
    }

    public static int fromRoman(String romanNumeral) {
        int result = 0;
        ArrayList<String> letters = (ArrayList<String>) Arrays.stream(romanNumeral.split("")).toList();

        for (int i = 0; i < letters.size(); i++) {
            if (letters.get(i).equals("M")) {
                result += 1000;
            } else if (letters.get(i).equals("D")) {
                result += 500;
            } else if (letters.get(i).equals("C") && letters.get(i + 1).equals("D")) {
                result += 400;
            } else if (letters.get(i).equals("C") && letters.get(i + 1).equals("M")) {
                result += 900;
            }
        }


        return 1;
    }
}