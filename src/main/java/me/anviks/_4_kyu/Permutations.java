package me.anviks._4_kyu;

import java.util.ArrayList;
import java.util.List;


/**
 * <a href="https://www.codewars.com/kata/5254ca2719453dcc0b00027d"><h2>So Many Permutations!</h2></a>
 * <p>
 * In this kata you have to create all permutations of an input string and remove duplicates, if present.
 * This means, you have to shuffle all letters from the input in all possible orders.
 * </p>
 * <h3>Examples:</h3>
 * <pre>
 * <code>With input "a":</code>
 * <code>Your function should return: ["a"]</code>
 *
 * <code>With input "ab":</code>
 * <code>Your function should return: ["ab", "ba"]</code>
 *
 * <code>With input "abc":</code>
 * <code>Your function should return: ["abc", "acb", "bac", "bca", "cab", "cba"]</code>
 *
 * <code>With input "aabb":</code>
 * <code>Your function should return: ["aabb", "abab", "abba", "baab", "baba", "bbaa"]</code>
 * </pre>
 * <p>
 * Note: The order of the permutations doesn't matter.
 * </p>
 * <p>
 * Good luck!
 * </p>
 */
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

    public static void main(String[] args) {
        System.out.println(singlePermutations("a"));  // [a]
        System.out.println(singlePermutations("ab"));  // [ab, ba]
        System.out.println(singlePermutations("abc"));  // [abc, acb, bac, bca, cab, cba]
        System.out.println(singlePermutations("aabb"));  // [aabb, abab, abba, baab, baba, bbaa]
    }
}
