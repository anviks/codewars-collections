package me.anviks._6_kyu;

/**
 * <a href="https://www.codewars.com/kata/525f50e3b73515a6db000b83/java"><h2>Create Phone Number</h2></a>
 * <p>
 * Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers
 * in the form of a phone number.
 * </p>
 * <p>
 * Example:
 * </p>
 * <pre>
 * <code>Kata.createPhoneNumber(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}) // => returns "(123) 456-7890"</code>
 * </pre>
 * <p>
 * The returned format must be correct in order to complete this challenge.
 * </p>
 * <p>
 * Don't forget the space after the closing parentheses!
 * </p>
 */
public class PhoneNumber {
    public static String createPhoneNumber(int[] numbers) {
        return "(" + numbers[0] + numbers[1] + numbers[2] + ") " + numbers[3] + numbers[4] + numbers[5] + "-" + numbers[6] + numbers[7] + numbers[8] + numbers[9];
    }

    public static void main(String[] args) {
        System.out.println(createPhoneNumber(new int[]{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}));
        System.out.println(createPhoneNumber(new int[]{1, 1, 1, 1, 1, 1, 1, 1, 1, 1}));
    }
}
