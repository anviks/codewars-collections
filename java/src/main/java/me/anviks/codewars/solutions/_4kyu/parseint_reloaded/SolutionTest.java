/*
 * https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
 */

package me.anviks.codewars.solutions._4kyu.parseint_reloaded;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import org.junit.runners.JUnit4;


public class SolutionTest {
    
    @Test
    public void fixedTests() {
        assertEquals(1 , Parser.parseInt("one"));
        assertEquals(20 , Parser.parseInt("twenty"));
        assertEquals(246 , Parser.parseInt("two hundred forty-six"));
        assertEquals(783919, Parser.parseInt("seven hundred eighty-three thousand nine hundred and nineteen"));
    }
}
