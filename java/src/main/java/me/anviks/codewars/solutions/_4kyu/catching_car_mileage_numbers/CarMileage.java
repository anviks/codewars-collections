/*
 * https://www.codewars.com/kata/52c4dd683bfd3b434c000292
 */

package me.anviks.codewars.solutions._4kyu.catching_car_mileage_numbers;


import java.util.Arrays;

public class CarMileage {

    private static boolean hasTrailingZeroes(int number) {
        var str = String.valueOf(number);
        return Integer.parseInt(str.substring(1)) == 0;
    }

    private static boolean hasOnlyOneDigit(int number) {
        var str = String.valueOf(number);
        return str.chars().distinct().count() == 1;
    }

    private static boolean hasSequentialDigits(int number, int direction) {
        var str = String.valueOf(number);
        char[] charArray = str.toCharArray();
        char previous = charArray[0];

        for (int i = 1; i < charArray.length; i++) {
            if (charArray[i] - previous != direction && !(direction == 1 && previous == '9' && charArray[i] == '0'))
                return false;
            previous = charArray[i];
        }

        return true;
    }

    private static boolean isPalindrome(int number) {
        var str = String.valueOf(number);
        char[] charArray = str.toCharArray();

        for (int i = 0; i < (charArray.length + 1) / 2; i++) {
            if (charArray[i] != charArray[charArray.length - i - 1]) return false;
        }

        return true;
    }

    private static boolean isAwesomePhrase(int number, int[] awesomePhrases) {
        return Arrays.stream(awesomePhrases).boxed().toList().contains(number);
    }

    private static boolean isNumberInteresting(int number, int[] awesomePhrases) {
        return number >= 100 && (
                hasTrailingZeroes(number)
                        || hasOnlyOneDigit(number)
                        || hasSequentialDigits(number, 1)
                        || hasSequentialDigits(number, -1)
                        || isPalindrome(number)
                        || isAwesomePhrase(number, awesomePhrases)
        );
    }

    public static int isInteresting(int number, int[] awesomePhrases) {
        if (isNumberInteresting(number, awesomePhrases)) return 2;
        if (isNumberInteresting(number + 1, awesomePhrases)) return 1;
        if (isNumberInteresting(number + 2, awesomePhrases)) return 1;

        return 0;
    }
}
