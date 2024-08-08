/*
 * https://www.codewars.com/kata/55fd2d567d94ac3bc9000064
 */

package me.anviks.codewars.solutions._7kyu.sum_of_odd_numbers;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class RowSumOddNumbersTest {

    @Test
    public void test1() {
        assertEquals(1, RowSumOddNumbers.rowSumOddNumbers(1));
        assertEquals(74088, RowSumOddNumbers.rowSumOddNumbers(42));
    }
}
