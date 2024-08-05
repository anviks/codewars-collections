/*
 * https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
 */

package me.anviks.codewars.solutions._7kyu.mumbling;

public class Accumul {
    public static String accum(String s) {
        StringBuilder r = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            r.append(s.substring(i, i + 1).toUpperCase());
            for (int j = 0; j < i; j++) {
                r.append(s.substring(i, i + 1).toLowerCase());
            }
            r.append("-");
        }
        return r.substring(0, r.length() - 1);
    }
}
