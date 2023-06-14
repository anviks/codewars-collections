package me.anviks._7_kyu;

import java.util.List;


/**
 * <a href="https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/java"><h2>List Filtering</h2></a>
 * <p>
 * In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list
 * with the strings filtered out.
 * </p>
 * Example:
 * <pre>
 * <code>filter_list([1,2,'a','b']) == [1,2]</code>
 * <code>filter_list([1,'a','b',0,15]) == [1,0,15]</code>
 * <code>filter_list([1,2,'aasf','1','123',123]) == [1,2,123]</code>
 * </pre>
 */
public class ListFiltering {
    public static List<Object> filterList(final List<Object> list) {
        return list.stream().filter((Object element) -> element instanceof Integer).toList();
    }

    public static void main(String[] args) {
        System.out.println(filterList(List.of(1, 2, "a", "b")));  // [1, 2]
        System.out.println(filterList(List.of(1, "a", "b", 0, 15)));  // [1, 0, 15]
        System.out.println(filterList(List.of(1, 2, "aasf", "1", "123", 123)));  // [1, 2, 123]
    }
}
