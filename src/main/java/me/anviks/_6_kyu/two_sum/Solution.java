package me.anviks._6_kyu.two_sum;

/*
 * https://www.codewars.com/kata/52c31f8e6605bcc646000082
 */

public class Solution {
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
}
