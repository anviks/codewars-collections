package me.anviks._6_kyu.build_tower;

/*
 * https://www.codewars.com/kata/576757b1df89ecf5bd00073b
 */

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SolutionTest {
    @Test
    public void basicTests() {
        assertEquals(String.join(",", "*"), String.join(",", Kata.towerBuilder(1)));
        assertEquals(String.join(",", " * ", "***"), String.join(",", Kata.towerBuilder(2)));
        assertEquals(String.join(",", "  *  ", " *** ", "*****"), String.join(",", Kata.towerBuilder(3)));
    }
}
