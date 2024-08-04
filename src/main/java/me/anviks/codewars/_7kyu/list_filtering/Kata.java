/*
 * https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
 */

package me.anviks.codewars._7kyu.list_filtering;

import java.util.List;

public class Kata {
    public static List<Object> filterList(final List<Object> list) {
        return list.stream().filter((Object element) -> element instanceof Integer).toList();
    }
}

