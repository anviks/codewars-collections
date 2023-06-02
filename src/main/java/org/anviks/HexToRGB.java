package org.anviks;

import java.util.Arrays;

public class HexToRGB {

    public static int[] hexStringToRGB(String hex) {
        hex = hex.toLowerCase().substring(1);
        return new int[]{Integer.parseInt(hex.substring(0, 2), 16),
                Integer.parseInt(hex.substring(2, 4), 16),
                Integer.parseInt(hex.substring(4, 6), 16)};
    }

    public static void main(String[] args) {

        System.out.println(Arrays.toString(hexStringToRGB("#FF9933")));  // {255, 153, 51}
        System.out.println(Arrays.toString(hexStringToRGB("#111111")));  // {17, 17, 17}
        System.out.println(Arrays.toString(hexStringToRGB("#000000")));  // {0, 0, 0}

    }

}
