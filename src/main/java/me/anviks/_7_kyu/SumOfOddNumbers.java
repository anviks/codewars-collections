package me.anviks._7_kyu;


/**
 * <a href="https://www.codewars.com/kata/55fd2d567d94ac3bc9000064/java"><h2>Sum of odd numbers</h2></a>
 * <p>
 * Given the triangle of consecutive odd numbers:
 * </p>
 * <pre>
 * <code>             1</code>
 * <code>          3     5</code>
 * <code>       7     9    11</code>
 * <code>   13    15    17    19</code>
 * <code>21    23    25    27    29</code>
 * <code>...</code>
 * </pre>
 * <p>
 * Calculate the row sums of this triangle from the row index (starting at index 1) e.g.:
 * </p>
 * <pre>
 * <code>rowSumOddNumbers(1); // 1</code>
 * <code>rowSumOddNumbers(2); // 3 + 5 = 8</code>
 * <code>rowSumOddNumbers(3); // 7 + 9 + 11 = 27</code>
 * <code>rowSumOddNumbers(4); // 13 + 15 + 17 + 19 = 64</code>
 * </pre>
 */
public class SumOfOddNumbers {
    public static int rowSumOddNumbers(int n) {
        return n * n * n;
    }
}
