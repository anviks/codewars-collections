/*
 * https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1
 */

package me.anviks.codewars._4kyu.snail;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Snail {
    public static int[] snail(int[][] array) {
        return helper(array).stream().mapToInt(Integer::intValue).toArray();
    }

    private static List<Integer> helper(int[][] array) {
        int size = array.length;
        List<Integer> result = new ArrayList<>();

        if (Arrays.deepEquals(array, new int[][]{{}})) {
            return List.of();
        }

        if (size == 1) {
            result.add(array[0][0]);
            return result;
        }

        for (int i = 0; i < size - 1; i++) {
            result.add(array[0][i]);
        }

        for (int i = 0; i < size - 1; i++) {
            result.add(array[i][size - 1]);
        }

        for (int i = size - 1; i > 0; i--) {
            result.add(array[size - 1][i]);
        }

        for (int i = size - 1; i > 0; i--) {
            result.add(array[i][0]);
        }

        if (size > 2) {
            int[][] innerArray = new int[size - 2][size - 2];

            for (int i = 1; i < size - 1; i++) {
                for (int j = 1; j < size - 1; j++) {
                    innerArray[i - 1][j - 1] = array[i][j];
                }
            }

            result.addAll(helper(innerArray));
        }

        return result;
    }
}
