/*
 * https://www.codewars.com/kata/576757b1df89ecf5bd00073b
 */

package me.anviks.codewars._6kyu.build_tower;

public class Kata {
    public static String[] towerBuilder(int nFloors) {
        String[] pyramid = new String[nFloors];
        for (int i = 0; i < nFloors; i++) {
            int spaceCount = (nFloors * 2 - (i * 2 + 1)) / 2;
            pyramid[i] = " ".repeat(spaceCount)
                    + "*".repeat(i * 2 + 1)
                    + " ".repeat(spaceCount);
        }
        return pyramid;
    }
}
