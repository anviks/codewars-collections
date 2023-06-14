package me.anviks._6_kyu;

import java.util.Arrays;


/**
 * <a href="https://www.codewars.com/kata/576757b1df89ecf5bd00073b/java"><h2>Build Tower</h2></a>
 * <p>
 * Build a pyramid-shaped tower, as an array/list of strings, given a positive integer "number of floors".
 * A tower block is represented with "*" character.
 * </p>
 * <p>
 * For example, a tower of 3 floors looks like this:
 * </p>
 * <pre>
 * <code>[
 * <code>  '  *  ',
 * <code>  ' *** ',
 * <code>  '*****'
 * <code>]</code>
 * </pre>
 * <p>
 * And a tower of 6 floors looks like this:
 * </p>
 * <pre>
 * <code>[
 * <code>  '     *     ',
 * <code>  '    ***    ',
 * <code>  '   *****   ',
 * <code>  '  *******  ',
 * <code>  ' ********* ',
 * <code>  '***********'
 * <code>]</code>
 * </pre>
 * <p>
 * Go challenge <a href="https://www.codewars.com/kata/57675f3dedc6f728ee000256"><strong>Build Tower Advanced</strong></a> once you have finished this :)
 * </p>
 */
public class BuildTower {
    public static String[] towerBuilder(int nFloors) {
        String[] pyramid = new String[nFloors];
        for (int i = 0; i < nFloors; i++) {
            pyramid[i] = " ".repeat((nFloors * 2 - (i * 2 + 1)) / 2) + "*".repeat(i * 2 + 1) + " ".repeat((nFloors * 2 - (i * 2 + 1)) / 2);
        }
        return pyramid;
    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(towerBuilder(3)));
        System.out.println(Arrays.toString(towerBuilder(6)));
    }
}
