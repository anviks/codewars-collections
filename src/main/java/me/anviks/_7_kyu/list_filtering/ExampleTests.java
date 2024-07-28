package me.anviks._7_kyu.list_filtering;

/*
 * https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
 */

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ExampleTests {

    @Test
    public void examples() {
        assertEquals(List.of(1, 2), Kata.filterList(List.of(1, 2, "a", "b")), "For input: [1, 2, \"a\", \"b\"]");
        assertEquals(List.of(1, 0, 15), Kata.filterList(List.of(1, "a", "b", 0, 15)), "For input: [1, \"a\", \"b\", 0, 15]");
        assertEquals(List.of(1, 2, 123), Kata.filterList(List.of(1, 2, "aasf", "1", "123", 123)), "For input: [1, 2, \"aasf\", \"1\", \"123\", 123]");
    }
}
