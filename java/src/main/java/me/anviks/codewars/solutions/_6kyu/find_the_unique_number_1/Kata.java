/*
 * https://www.codewars.com/kata/585d7d5adb20cf33cb000235
 */

package me.anviks.codewars.solutions._6kyu.find_the_unique_number_1;

import java.util.Arrays;

// Make sure your class is public
public class Kata {
    public static double findUniq(double[] arr) {
        double idk = 0;
        for (double i : Arrays.stream(arr).distinct().toArray()) {
            if (i == arr[0] && i == arr[1] || i == arr[0] && i == arr[2] || i == arr[1] && i == arr[2]) continue;
            idk = i;
        }
        return idk;
    }
}
