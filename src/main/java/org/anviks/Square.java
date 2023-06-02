package org.anviks;

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