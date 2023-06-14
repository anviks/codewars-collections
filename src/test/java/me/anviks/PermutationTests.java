package me.anviks;

import me.anviks._4_kyu.Permutations;
import org.junit.Test;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsInAnyOrder;

public class PermutationTests {

    @Test
    public void permutations() {
        assertThat(Permutations.singlePermutations("ab"), containsInAnyOrder("ab", "ba"));
        assertThat(Permutations.singlePermutations("a"), containsInAnyOrder("a"));
        assertThat(Permutations.singlePermutations("abc"), containsInAnyOrder("abc", "acb", "bac", "bca", "cab", "cba"));
        assertThat(Permutations.singlePermutations("aabb"), containsInAnyOrder("aabb", "abab", "abba", "baab", "baba", "bbaa"));
    }


}
