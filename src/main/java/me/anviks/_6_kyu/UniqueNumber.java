package me.anviks._6_kyu;

import java.util.Arrays;


/**
 * <a href="https://www.codewars.com/kata/585d7d5adb20cf33cb000235"><h2>Find the unique number</h2></a>
 * <p>
 * There is an array with some numbers. All numbers are equal except for one. Try to find it!
 * </p>
 * <pre>
 * <code>findUniq(new double[]{ 1, 1, 1, 2, 1, 1 }); // => 2</code>
 * <code>findUniq(new double[]{ 0, 0, 0.55, 0, 0 }); // => 0.55</code>
 * <code>findUniq(new double[]{ 3, 10, 3, 3, 3 }); // => 10</code>
 * </pre>
 * <p>
 * It’s guaranteed that array contains at least 3 numbers.
 * </p>
 * <p>
 * The tests contain some very huge arrays, so think about performance.
 * </p>
 * <p>
 * <h3>This is the first kata in series:</h3>
 * <ul>
 * <li><a href="https://www.codewars.com/kata/585d7d5adb20cf33cb000235">Find the unique number</a></li>
 * <li><a href="https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3">Find the unique string</a></li>
 * <li><a href="https://www.codewars.com/kata/5862e0db4f7ab47bed0000e5">Find The Unique</a></li>
 * </ul>
 * </p>
 */
public class UniqueNumber {
    public static double findUniq(double arr[]) {
        double idk = 0;
        for (double i : Arrays.stream(arr).distinct().toArray()) {
            if (i == arr[0] && i == arr[1] || i == arr[0] && i == arr[2] || i == arr[1] && i == arr[2]) continue;
            idk = i;
        }
        return idk;
    }

    public static void main(String[] args) {
        System.out.println(findUniq(new double[]{1, 1, 1, 2, 1, 1})); // 2
        System.out.println(findUniq(new double[]{0, 0, 0.55, 0, 0})); // 0.55
        System.out.println(findUniq(new double[]{3, 10, 3, 3, 3})); // 10
    }
}
