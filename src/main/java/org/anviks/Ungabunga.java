package org.anviks;

import java.lang.annotation.ElementType;
import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;


public class Ungabunga {
    public static void main(String[] args) {
        System.out.println(Double.NEGATIVE_INFINITY * Double.NEGATIVE_INFINITY);
        System.out.println(Math.random() * 20 + 1);
//        * (max - min) + min
        List<Object> list = new ArrayList<>(List.of(1, 2, "a", "b"));
        list.removeIf((Object element) -> element instanceof String);
        System.out.println(list);
        System.out.println(list.stream().filter(element -> element instanceof Integer).toList());
        System.out.println(accum("fuck"));
        StringBuilder u = new StringBuilder();
        System.out.println(solution(1666));
        System.out.println(System.currentTimeMillis());
        HashSet<Integer> set = new HashSet<Integer>();
        set.add(4);
        set.add(6);
        set.addAll((Collection<Integer>) List.of(2, 1, 4, 7, 8));
        System.out.println(set);
        HashMap<String, ArrayList<String>> idk = new HashMap<>();
        idk.put("lol", new ArrayList<>());
        idk.get("lol").add("s");
        idk.get("lol").add("g");
        idk.put("fff", new ArrayList<>());
        idk.get("fff").add("x");
        idk.get("fff").add("z");
        idk.get("fff").add("l");
        idk.put("ffsdaf", new ArrayList<>());
        idk.get("ffsdaf").add("x");
        idk.get("fff").add("z");
        idk.get("fff").add("l");

        System.out.println(idk.values().stream().mapToInt(ArrayList::size).max());

        String d = "942";
        int g = Integer.parseInt(d);
        var s = "sd";

        System.out.println(40 + "sss" + 52.342d);

        System.out.println(Math.pow(2, 5));
        ArrayList<Integer> ssda = new ArrayList<>();

        System.out.println(josephusSurvivor(7, 3));

        System.out.println("sda" + 2);

        System.out.println(Integer.parseInt("1234".charAt(1) + ""));
    }

    public static String accum(String s) {
        StringBuilder r = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            r.append(s.substring(i, i + 1).toUpperCase());
            r.append(s.substring(i, i + 1).toLowerCase().repeat(i));
            r.append("-");
        }
        return r.substring(0, r.length() - 1);
    }

    public static String solution(int n) {
        StringBuilder b = new StringBuilder();
        b.append("M".repeat(n / 1000));
        n %= 1000;
        b.append("CM".repeat(n / 900));
        n %= 900;
        b.append("D".repeat(n / 500));
        n %= 500;
        b.append("CD".repeat(n / 400));
        n %= 400;
        b.append("C".repeat(n / 100));
        n %= 100;
        b.append("XC".repeat(n / 90));
        n %= 90;
        b.append("L".repeat(n / 50));
        n %= 50;
        b.append("XL".repeat(n / 40));
        n %= 40;
        b.append("X".repeat(n / 10));
        n %= 10;
        b.append("IX".repeat(n / 9));
        n %= 9;
        b.append("V".repeat(n / 5));
        n %= 5;
        b.append("IV".repeat(n / 4));
        n %= 4;
        b.append("I".repeat(n));
        return b.toString();
    }

    public static int josephusSurvivor(final int n, final int k) {
        ArrayList<Integer> survivors = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            survivors.add(i);
        }
        for (int i = k - 1; i > -1; i += k - 1) {
            if (survivors.size() == 1) {
                break;
            }
            survivors.remove(i %= (survivors.size()));
        }
        return survivors.get(0);
    }
}

