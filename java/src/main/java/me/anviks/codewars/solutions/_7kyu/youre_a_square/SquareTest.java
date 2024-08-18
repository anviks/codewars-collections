/*
 * https://www.codewars.com/kata/54c27a33fb7da0db0100040e
 */

package me.anviks.codewars.solutions._7kyu.youre_a_square;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class SquareTest {
    @Test
    public void shouldWorkForSomeExamples() throws Exception {
        assertFalse(Square.isSquare(-1), "negative numbers aren't square numbers");
        assertTrue(Square.isSquare(0), "0 is a square number (0 * 0)");
        assertFalse(Square.isSquare(3), "3 isn't a square number");
        assertTrue(Square.isSquare(4), "4 is a square number (2 * 2)");
        assertTrue(Square.isSquare(25), "25 is a square number (5 * 5)");
        assertFalse(Square.isSquare(26), "26 isn't a square number");
    }
}
