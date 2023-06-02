package org.anviks;

import java.io.*;
import java.util.Scanner;

public class FileHandling {

    public static void createFile(String fileName) {
        try {
            File file = new File(fileName);
            if (file.createNewFile()) {
                System.out.println("File created with the name of " + fileName);
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }

    public static String readFile(String fileName) {
        try {
            File file = new File(fileName);
            Scanner scanner = new Scanner(file);
            while (scanner.hasNextLine()) {
                System.out.println(scanner.nextLine());
            }
            return " ";
        } catch (FileNotFoundException e) {
            return e.getMessage();
        }
    }

    public static void writeFile(String fileName, String message) {
        try {
            FileWriter writer = new FileWriter(fileName, true);
            writer.write(message + "\n");
            writer.close();
        } catch (IOException e) {
            System.out.println("An error occurred.");
            System.out.println(e.getMessage());
        }
    }

    public static void main(String[] args) {
        createFile("somefile.txt");
        writeFile("somefile.txt", "nasty shit");
        System.out.println(readFile("somefile.txt"));
    }
}
