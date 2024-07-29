package me.anviks.codewars._6kyu.roman_numerals_encoder;

/*
 * https://www.codewars.com/kata/51b62bf6a9c58071c600001b
 */

public class Conversion {
    public String solution(int n) {
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
}
