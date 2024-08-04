/*
 * https://www.codewars.com/kata/54c27a33fb7da0db0100040e
 */

package me.anviks.codewars._7kyu.you_re_a_square;

public class Square {
    public static boolean isSquare(int n) {
        return Math.sqrt(n) == (int) Math.sqrt(n);
    }
}
