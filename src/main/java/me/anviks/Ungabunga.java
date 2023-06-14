package me.anviks;

import java.util.*;


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
}

