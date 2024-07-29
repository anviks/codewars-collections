package me.anviks.codewars._5kyu.josephus_survivor;

/*
 * https://www.codewars.com/kata/555624b601231dc7a400017a
 */

import java.util.ArrayList;

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
