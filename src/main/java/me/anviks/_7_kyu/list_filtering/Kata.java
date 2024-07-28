package me.anviks._7_kyu.list_filtering;

/*
 * https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
 */

import java.util.List;

public class Kata {
    public static List<Object> filterList(final List<Object> list) {
        return list.stream().filter((Object element) -> element instanceof Integer).toList();
    }
}

