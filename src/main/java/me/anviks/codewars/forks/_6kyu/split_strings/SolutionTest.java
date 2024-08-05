/*
 * https://www.codewars.com/kumite/5817876f6288540b10000d6d?sel=66affe5ecb6226982fd7a4f5
 */

package me.anviks.codewars.forks._6kyu.split_strings;

import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class SolutionTest {
    @Test
    public void testEmptyString() {
        String s = "";
        assertArrayEquals(new String[]{}, StringSplit.solution(s), "Should handle empty string");
    }

    @Test
    public void testEvenString() {
        String s = "abcdef";
        String s1 = "HelloWorld";
        assertArrayEquals(new String[]{"ab", "cd", "ef"}, StringSplit.solution(s), "Should handle even string");
        assertArrayEquals(new String[]{"He", "ll", "oW", "or", "ld"}, StringSplit.solution(s1), "Should handle even string");
    }

    @Test
    public void testOddString() {
        String s = "abcde";
        String s1 = "LovePizza";
        assertArrayEquals(new String[]{"ab", "cd", "e_"}, StringSplit.solution(s), "Should handle odd string");
        assertArrayEquals(new String[]{"Lo", "ve", "Pi", "zz", "a_"}, StringSplit.solution(s1), "Should handle odd string");
    }

    @Test
    public void testSpaceString() {
        String s = "Hello World";
        String s1 = "I Love Pizza";
        assertArrayEquals(new String[]{"He", "ll", "o ", "Wo", "rl", "d_"}, StringSplit.solution(s), "Should handle space in string");
        assertArrayEquals(new String[]{"I ", "Lo", "ve", " P", "iz", "za"}, StringSplit.solution(s1), "Should handle space in string");
    }

    private final Random rand = new Random();

    private char randomChar() {
        String alphabet = "abcdefghijklmnopqrstuvwxyz1234567890    ";
        return alphabet.charAt(rand.nextInt(alphabet.length()));
    }

    @Test
    public void randomTests() {
        for (int trial = 1; trial <= 100; trial++) {
            String[] expected = new String[rand.nextInt(21)];
            for (int i = 0; i < expected.length; i++)
                expected[i] = "" + randomChar() + randomChar();
            if (0 < expected.length && rand.nextBoolean())
                expected[expected.length - 1] = randomChar() + "_";
            StringBuilder sb = new StringBuilder();
            for (String string : expected) sb.append(string);
            String[] actual = StringSplit.solution(sb.toString().replace("_$", ""));
            assertArrayEquals(expected, actual,
                    "Expected: " + Arrays.toString(expected) + " but got: " + Arrays.toString(actual));
        }
    }
}
