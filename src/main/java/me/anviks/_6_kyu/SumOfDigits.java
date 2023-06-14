package me.anviks._6_kyu;


/**
 * <a href="https://www.codewars.com/kata/541c8630095125aba6000c00"><h2>Sum of Digits / Digital Root</h2></a>
 * <p>
 * <a href="https://en.wikipedia.org/wiki/Digital_root">Digital root</a> is the recursive sum of all the digits in a number.
 * </p>
 * <p>
 * Given <code>n</code>, take the sum of the digits of <code>n</code>. If that value has more than one digit, continue
 * reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
 * </p>
 * <p>
 * Examples:
 * </p>
 * <pre>
 * <code>16  --&gt;  1 + 6 = 7</code>
 * <code>942  --&gt;  9 + 4 + 2 = 15  --&gt;  1 + 5 = 6</code>
 * <code>132189  --&gt;  1 + 3 + 2 + 1 + 8 + 9 = 24  --&gt;  2 + 4 = 6</code>
 * <code>493193  --&gt;  4 + 9 + 3 + 1 + 9 + 3 = 29  --&gt;  2 + 9 = 11</code>
 * </pre>
 */
public class SumOfDigits {
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

    public static void main(String[] args) {
        System.out.println(digital_root(16));
        System.out.println(digital_root(942));
        System.out.println(digital_root(132189));
        System.out.println(digital_root(493193));
    }
}
