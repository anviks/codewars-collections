/*
 * https://www.codewars.com/kata/51b62bf6a9c58071c600001b
 */

package me.anviks.codewars.solutions._6kyu.roman_numerals_encoder;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ConversionTest {

    private Conversion conversion = new Conversion();

    @Test
    public void shouldConvertToRoman() {
        assertEquals("solution(1) should equal to I", "I", conversion.solution(1));
        assertEquals("solution(4) should equal to IV", "IV", conversion.solution(4));
        assertEquals("solution(6) should equal to VI", "VI", conversion.solution(6));
    }
}

