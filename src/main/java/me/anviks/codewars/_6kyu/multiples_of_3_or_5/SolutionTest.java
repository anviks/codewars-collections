package me.anviks.codewars._6kyu.multiples_of_3_or_5;

/*
 * https://www.codewars.com/kata/514b92a657cdc65150000006
 */

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void test() {
        assertEquals(23, new Solution().solution(10));
    }
}
