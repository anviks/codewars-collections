/*
 * https://www.codewars.com/kata/541c8630095125aba6000c00
 */

package me.anviks.codewars.solutions._6kyu.sum_of_digits_digital_root;

public class DRoot {
    public static int digital_root(int n) {
        if (("" + n).length() > 1) {
            int m = 0;
            for (int i = 0; i < ("" + n).length(); i++) {
                m += Integer.parseInt(("" + n).substring(i, i + 1));
            }
            return digital_root(m);
        }
        return n;
    }
}
