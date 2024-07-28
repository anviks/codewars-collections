package me.anviks._6_kyu.multiples_of_3_or_5;

/*
 * https://www.codewars.com/kata/514b92a657cdc65150000006
 */

import java.util.stream.IntStream;

public class Solution {
    public int solution(int number) {
        return IntStream.range(1, number).filter(i -> i % 3 == 0 || i % 5 == 0).sum();
    }
}
