package me.anviks._6_kyu;

/**
 * <a href="https://www.codewars.com/kata/5266876b8f4bf2da9b000362/java"><h2>Who likes it?</h2></a>
 * <p>
 * You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
 * items. We want to create the text that should be displayed next to such an item.
 * </p>
 * <p>
 * Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who
 * like an item. It must return the display text as shown in the examples:
 * </p>
 * <ul>
 *     <li>likes {} // must be "no one likes this"</li>
 *     <li>likes {"Peter"} // must be "Peter likes this"</li>
 *     <li>likes {"Jacob", "Alex"} // must be "Jacob and Alex like this"</li>
 *     <li>likes {"Max", "John", "Mark"} // must be "Max, John and Mark like this"</li>
 *     <li>likes {"Alex", "Jacob", "Mark", "Max"} // must be "Alex, Jacob and 2 others like this"</li>
 *     <li>For 4 or more names, the number in "and 2 others" simply increases.</li>
 * </ul>
 */
public class WhoLikesIt {
    public static String whoLikesIt(String... names) {
        if (names.length == 0) {
            return "no one likes this";
        } else if (names.length == 1) {
            return names[0] + " likes this";
        } else if (names.length == 2) {
            return String.format("%s and %s like this", names[0], names[1]);
        } else if (names.length == 3) {
            return String.format("%s, %s and %s like this", names[0], names[1], names[2]);
        } else {
            return String.format("%s, %s and %s others like this", names[0], names[1], names.length - 2);
        }
    }

    public static void main(String[] args) {
        System.out.println(whoLikesIt());
        System.out.println(whoLikesIt("Peter"));
        System.out.println(whoLikesIt("Jacob", "Alex"));
        System.out.println(whoLikesIt("Max", "John", "Mark"));
        System.out.println(whoLikesIt("Alex", "Jacob", "Mark", "Max"));
        System.out.println(whoLikesIt("Alex", "Jacob", "Mark", "Max", "John"));
    }
}
