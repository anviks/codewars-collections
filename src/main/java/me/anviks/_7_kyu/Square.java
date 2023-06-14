package me.anviks._7_kyu;


/**
 * <a href="https://www.codewars.com/kata/54c27a33fb7da0db0100040e"><h2>You're a square!</h2></a>
 * <h3>Task:</h3>
 * <p>
 * Given an integral number, determine if it's a square number:
 * </p>
 * <pre>
 * <code>In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words,
 * it is the product of some integer with itself.</code>
 * </pre>
 * <h3>Examples:</h3>
 * <pre>
 * <code>isSquare(-1) // => false</code>
 * <code>isSquare( 0) // => true</code>
 * <code>isSquare( 3) // => false</code>
 * <code>isSquare( 4) // => true</code>
 * <code>isSquare(25) // => true</code>
 * <code>isSquare(26) // => false</code>
 * </pre>
 */
public class Square {
    public static boolean isSquare(int n) {
        return Math.sqrt(n) == (int) Math.sqrt(n);
    }

    public static void main(String[] args) {
        // 7 kyu task lmao.
        System.out.println(isSquare(-4));
        System.out.println(isSquare(124));
        System.out.println(isSquare(9));
    }
}
