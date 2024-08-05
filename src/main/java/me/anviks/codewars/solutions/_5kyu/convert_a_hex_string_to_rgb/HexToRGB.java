/*
 * https://www.codewars.com/kata/5282b48bb70058e4c4000fa7
 */

package me.anviks.codewars.solutions._5kyu.convert_a_hex_string_to_rgb;

import java.util.Map;

public class HexToRGB {
    public static Map<String, Integer> hexStringToRGB(String hex) {
        hex = hex.toLowerCase().substring(1);
        return Map.of(
                "r", Integer.parseInt(hex.substring(0, 2), 16),
                "g", Integer.parseInt(hex.substring(2, 4), 16),
                "b", Integer.parseInt(hex.substring(4, 6), 16)
        );
    }
}
