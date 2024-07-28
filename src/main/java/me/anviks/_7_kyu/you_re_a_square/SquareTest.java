package me.anviks._7_kyu.you_re_a_square;

/*
 * https://www.codewars.com/kata/54c27a33fb7da0db0100040e
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import java.util.Random;

public class SquareTest {
    @Test
    public void shouldWorkForSomeExamples() throws Exception {
      assertEquals("negative numbers aren't square numbers", false, Square.isSquare(-1));
      assertEquals("0 is a square number (0 * 0)",    true,   Square.isSquare(0));
      assertEquals("3 isn't a square number", false,  Square.isSquare(3));
      assertEquals("4 is a square number (2 * 2)",    true,   Square.isSquare(4));
      assertEquals("25 is a square number (5 * 5)",   true,   Square.isSquare(25));
      assertEquals("26 isn't a square number",false,  Square.isSquare(26));      
    }
}
