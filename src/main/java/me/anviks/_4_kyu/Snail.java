package me.anviks._4_kyu;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


/**
 * <a href="https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1"><h2>Snail</h2></a>
 * <p>
 * Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
 * </p>
 * <pre>
 * array = [[1,2,3],
 *         [4,5,6],
 *         [7,8,9]]
 * snail(array) #=> [1,2,3,6,9,8,7,4,5]
 * </pre>
 * <p>
 * For better understanding, please follow the numbers of the next array consecutively:
 * </p>
 * <pre>
 * array = [[1,2,3],
 *         [8,9,4],
 *         [7,6,5]]
 * snail(array) #=> [1,2,3,4,5,6,7,8,9]
 * </pre>
 * <p>
 * This image will illustrate things more clearly:
 * </p>
 * <img src="https://static.wikia.nocookie.net/breakingbad/images/e/e0/Saul_2009.jpg/revision/latest?cb=20220812220131" width=600 height=150 alt="Snail">
 * <p>
 * NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.
 * </p>
 * <p>
 * NOTE 2: The 0x0 (empty matrix) is represented as [[]]
 * </p>
 */
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

    public static void main(String[] args) {
        System.out.println(Arrays.toString(snail(new int[][]{{1, 2, 3}, {8, 9, 4}, {7, 6, 5}})));
        System.out.println(Arrays.toString(snail(new int[][]{{5, 9, 4, 1}, {6, 8, 1, 2}, {5, 9, 4, 1}, {6, 8, 1, 2}})));
        System.out.println(Arrays.toString(snail(new int[][]{{1, 2, 3, 4, 5}, {16, 17, 18, 19, 6}, {15, 24, 25, 20, 7}, {14, 23, 22, 21, 8}, {13, 12, 11, 10, 9}})));
    }
}