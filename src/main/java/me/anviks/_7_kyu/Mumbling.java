package me.anviks._7_kyu;


/**
 * <a href="https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/java"><h2>Mumbling</h2></a>
 * <p>
 * This time no story, no theory. The examples below show you how to write function accum:
 * </p>
 * <pre>
 * <code>accum("abcd") -> "A-Bb-Ccc-Dddd"</code>
 * <code>accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"</code>
 * <code>accum("cwAt") -> "C-Ww-Aaa-Tttt"</code>
 * </pre>
 * The parameter of accum is a string which includes only letters from a..z and A..Z.
 */
public class Mumbling {
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

    public static void main(String[] args) {
        System.out.println(accum("abcd"));
    }
}
