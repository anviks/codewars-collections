package me.anviks._6_kyu;

import java.util.Arrays;


/**
 * <a href="https://www.codewars.com/kata/52c31f8e6605bcc646000082"><h2>Two Sum</h2></a>
 * <p>
 * Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two
 * different items in the array that, when added together, give the target value. The indices of these items should
 * then be returned in a tuple like so: (index1, index2).
 * </p>
 * <p>
 * For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
 * </p>
 * <p>
 * The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be
 * numbers; target will always be the sum of two different items from that array).
 * </p>
 * <p>
 * Based on: <a href="http://oj.leetcode.com/problems/two-sum/">LeetCode - Two Sum</a>
 * </p>
 */
public class TwoSum {
    public static int[] twoSum(int[] numbers, int target) {
        int[] solution = new int[2];
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < numbers.length; j++) {
                if (numbers[i] + numbers[j] == target && i != j) {
                    solution[0] = i;
                    solution[1] = j;
                    break;
                }
            }
        }
        return solution;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(twoSum(new int[]{1, 2, 3}, 4)));  // {0, 2}
        System.out.println(Arrays.toString(twoSum(new int[]{1234, 5678, 9012}, 14690)));  // {1, 2}
        System.out.println(Arrays.toString(twoSum(new int[]{2, 2, 3}, 4)));  // {0, 1}
    }
}
