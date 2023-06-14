package me.anviks._5_kyu;

import java.util.ArrayList;


/**
 * <a href="https://www.codewars.com/kata/555624b601231dc7a400017a"><h2>Josephus Survivor</h2></a>
 * <p>
 * In this kata you have to correctly return who is the "survivor", ie: the last element of a <a href="http://www.codewars.com/kata/josephus-permutation/">Josephus permutation</a>.
 * </p>
 * <p>
 * Basically you have to assume that n people are put into a circle and that they are eliminated in steps of k elements, like this:
 * </p>
 * <pre>
 * <code> n=7 k=3 => means 7 people in a circle</code>
 * <code> one every 3 is eliminated until one remains</code>
 * <code> [1,2,3,4,5,6,7] - initial sequence</code>
 * <code> [1,2,4,5,6,7] => 3 is counted out</code>
 * <code> [1,2,4,5,7] => 6 is counted out</code>
 * <code> [1,4,5,7] => 2 is counted out</code>
 * <code> [1,4,5] => 7 is counted out</code>
 * <code> [1,4] => 5 is counted out</code>
 * <code> [4] => 1 counted out, 4 is the last element - the survivor!</code>
 * </pre>
 * <p>
 * The above link about the "base" kata description will give you a more thorough insight about the origin of this kind of permutation, but basically that's all that there is to know to solve this kata.
 * </p>
 * <p>
 * Notes and tips: using the solution to the other kata to check your function may be helpful, but as much larger numbers will be used, using an array/list to compute the number of the survivor may be too slow; you may assume that both n and k will always be >= 1.
 * </p>
 */
public class JosephusSurvivor {
    public static int josephusSurvivor(final int n, final int k) {
        ArrayList<Integer> survivors = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            survivors.add(i);
        }
        for (int i = k - 1; i > -1; i += k - 1) {
            if (survivors.size() == 1) {
                break;
            }
            survivors.remove(i %= (survivors.size()));
        }
        return survivors.get(0);
    }
}
