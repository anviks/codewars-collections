/*
 * https://www.codewars.com/kumite/5817876f6288540b10000d6d?sel=66affe5ecb6226982fd7a4f5
 */

package me.anviks.codewars.forks._6kyu.split_strings;

public class StringSplit {
    public static String[] solution(String s) {
        String[] solution = s.split("(?<=\\G..)");

        if (solution.length == 1 && "".equals(solution[0]))
            return new String[0];

        if (solution[solution.length - 1].length() == 1)
            solution[solution.length - 1] += "_";

        return solution;
    }
}
