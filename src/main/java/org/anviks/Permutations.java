package org.anviks;

import java.util.ArrayList;
import java.util.List;

public class Permutations {

    public static List<String> singlePermutations(String s) {
        List<String> permutations = new ArrayList<>();
        generatePermutations("", s, permutations);
        return permutations.stream().distinct().toList();
    }

    private static void generatePermutations(String prefix, String suffix, List<String> permutations) {
        int n = suffix.length();
        if (n == 0) {
            permutations.add(prefix);
        } else {
            for (int i = 0; i < n; i++) {
                generatePermutations(prefix + suffix.charAt(i),
                        suffix.substring(0, i) + suffix.substring(i + 1, n),
                        permutations);
            }
        }
    }

}
