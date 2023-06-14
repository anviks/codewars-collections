package me.anviks._5_kyu;


/**
 * <a href="https://www.codewars.com/kata/520b9d2ad5c005041100000f"><h2>Pig Latin</h2></a>
 * <p>
 * Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
 * </p>
 * <p>
 * <h3>Examples:</h3>
 * </p>
 * <pre>
 * <code>pigIt('Pig latin is cool'); // igPay atinlay siay oolcay</code>
 * <code>pigIt('Hello world !');     // elloHay orldway !</code>
 * </pre>
 */
public class PigLatin {
    public static String pigIt(String str) {
        StringBuilder pig = new StringBuilder();
        for (String word : str.split(" ")) {
            if ("?!.".contains(word)) {
                pig.append(" ").append(word);
                continue;
            }
            pig.append(" ").append(word.substring(1)).append(word.substring(0, 1)).append("ay");
        }
        return pig.substring(1);
    }

    public static void main(String[] args) {
        System.out.println(pigIt("Pig latin is cool"));  // igPay atinlay siay oolcay
        System.out.println(pigIt("Hello world !"));  // elloHay orldway !
    }
}
