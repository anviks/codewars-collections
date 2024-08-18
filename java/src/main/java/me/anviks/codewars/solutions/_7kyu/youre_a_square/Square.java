/*
 * https://www.codewars.com/kata/54c27a33fb7da0db0100040e
 */

package me.anviks.codewars.solutions._7kyu.youre_a_square;

public class Square {
    public static boolean isSquare(int n) {
        return Math.sqrt(n) == (int) Math.sqrt(n);
    }
}
