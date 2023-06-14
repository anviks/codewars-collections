package me.anviks._6_kyu;

import java.util.stream.IntStream;


/**
 * <a href="https://www.codewars.com/kata/514b92a657cdc65150000006/java"><h2>Multiples of 3 or 5</h2></a>
 * <p>
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6
 * and 9. The sum of these multiples is 23.
 * </p>
 * <p>
 * Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the
 * number passed in.
 * </p>
 * <p>
 * Note: If the number is a multiple of both 3 and 5, only count it once.
 * </p>
 */
public class Multiples3or5 {
    public static int solution(int number) {
        return IntStream.range(1, number).filter(i -> i % 3 == 0 || i % 5 == 0).sum();
    }

    public static int solution2(int number) {
        if (number <= 0) return 0;
        return (sumSeries(3, number) + sumSeries(5, number) - sumSeries(15, number));
    }

    public static int sumSeries(int factor, int number) {
        number -= 1; //excludes the given number
        int amount = (number) / factor;
        int first = factor;
        int last = (number) - (number) % factor;
//        System.out.println("sum of multiples of " + factor + ": " + (amount * (first + last)) / 2);
        return (amount * (first + last)) / 2;
    }

    public static void main(String[] args) {
        var start = System.currentTimeMillis();
        System.out.println(solution2(1_000_000_000));
        System.out.println(System.currentTimeMillis() - start);
        start = System.currentTimeMillis();
        System.out.println(solution(1_000_000_000));
        System.out.println(System.currentTimeMillis() - start);
    }
}
