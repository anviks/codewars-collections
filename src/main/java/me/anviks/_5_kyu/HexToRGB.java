package me.anviks._5_kyu;


import java.util.Map;

/**
 * <a href="https://www.codewars.com/kata/5282b48bb70058e4c4000fa7"><h2>RGB To Hex Conversion</h2></a>
 * <p>
 * When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color.
 * Implement a function that meets these requirements:
 * </p>
 * <ul>
 * <li>Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")</li>
 * <li>Returns a Map<String, Integer> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255</li>
 * </ul>
 * <p>
 * Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")
 * </p>
 * <p>
 * <h3>Example:</h3>
 * </p>
 * <pre>
 * <code>HexToRGB.hexStringToRGB("#FF9933") // returns {r: 255, g: 153, b: 51}</code>
 * </pre>
 */
public class HexToRGB {
    public static Map<String, Integer> hexStringToRGB(String hex) {
        hex = hex.toLowerCase().substring(1);
        return Map.of(
                "r", Integer.parseInt(hex.substring(0, 2), 16),
                "g", Integer.parseInt(hex.substring(2, 4), 16),
                "b", Integer.parseInt(hex.substring(4, 6), 16)
        );
    }

    public static void main(String[] args) {
        System.out.println(hexStringToRGB("#FF9933"));  // {r=255, g=153, b=51}
        System.out.println(hexStringToRGB("#111111"));  // {r=17, g=17, b=17}
        System.out.println(hexStringToRGB("#000000"));  // {r=0, g=0, b=0}
    }
}
