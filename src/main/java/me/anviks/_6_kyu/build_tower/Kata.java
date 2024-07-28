package me.anviks._6_kyu.build_tower;

/*
 * https://www.codewars.com/kata/576757b1df89ecf5bd00073b
 */

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
