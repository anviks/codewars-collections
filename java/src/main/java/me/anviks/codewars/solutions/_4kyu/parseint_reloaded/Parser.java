/*
 * https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5
 */

package me.anviks.codewars.solutions._4kyu.parseint_reloaded;


import java.util.ArrayList;
import java.util.List;
import java.util.Map;

import static java.util.Map.entry;

enum TokenType {
    LITERAL,
    HUNDRED,
    GROUP_BOUNDARY
}

class Token {
    TokenType type;
    int value;

    public Token(TokenType type, int value) {
        this.type = type;
        this.value = value;
    }

    @Override
    public String toString() {
        return "Token{" +
                "type=" + type +
                ", value=" + value +
                '}';
    }
}


class NumberLexer {
    private String data;
    private int pos = 0;

    private static final Map<String, Token> numbers = Map.ofEntries(
            entry("zero", new Token(TokenType.LITERAL, 0)),
            entry("one", new Token(TokenType.LITERAL, 1)),
            entry("two", new Token(TokenType.LITERAL, 2)),
            entry("three", new Token(TokenType.LITERAL, 3)),
            entry("four", new Token(TokenType.LITERAL, 4)),
            entry("five", new Token(TokenType.LITERAL, 5)),
            entry("six", new Token(TokenType.LITERAL, 6)),
            entry("seven", new Token(TokenType.LITERAL, 7)),
            entry("eight", new Token(TokenType.LITERAL, 8)),
            entry("nine", new Token(TokenType.LITERAL, 9)),
            entry("ten", new Token(TokenType.LITERAL, 10)),
            entry("eleven", new Token(TokenType.LITERAL, 11)),
            entry("twelve", new Token(TokenType.LITERAL, 12)),
            entry("thirteen", new Token(TokenType.LITERAL, 13)),
            entry("fourteen", new Token(TokenType.LITERAL, 14)),
            entry("fifteen", new Token(TokenType.LITERAL, 15)),
            entry("sixteen", new Token(TokenType.LITERAL, 16)),
            entry("seventeen", new Token(TokenType.LITERAL, 17)),
            entry("eighteen", new Token(TokenType.LITERAL, 18)),
            entry("nineteen", new Token(TokenType.LITERAL, 19)),
            entry("twenty", new Token(TokenType.LITERAL, 20)),
            entry("thirty", new Token(TokenType.LITERAL, 30)),
            entry("forty", new Token(TokenType.LITERAL, 40)),
            entry("fifty", new Token(TokenType.LITERAL, 50)),
            entry("sixty", new Token(TokenType.LITERAL, 60)),
            entry("seventy", new Token(TokenType.LITERAL, 70)),
            entry("eighty", new Token(TokenType.LITERAL, 80)),
            entry("ninety", new Token(TokenType.LITERAL, 90)),
            entry("hundred", new Token(TokenType.HUNDRED, 100)),
            entry("thousand", new Token(TokenType.GROUP_BOUNDARY, 1000)),
            entry("million", new Token(TokenType.GROUP_BOUNDARY, 1000000))
    );

    public NumberLexer(String data) {
        this.data = data;
    }

    public List<Token> getTokens() {
        List<Token> tokens = new ArrayList<>();

        while (!eof()) {
            String word = readWord();
            if (word.equals("and")) continue;
            tokens.add(numbers.get(word));
        }

        return tokens;
    }

    private String readWord() {
        StringBuilder sb = new StringBuilder();

        while (!eof() && lookahead() != ' ' && lookahead() != '-') {
            sb.append(consume());
        }

        pos++;

        return sb.toString();
    }

    private boolean eof() {
        return pos >= data.length();
    }

    private char consume() {
        return data.charAt(pos++);
    }

    private char lookahead() {
        return data.charAt(pos);
    }
}


public class Parser {
    public static int parseInt(String numStr) {
        NumberLexer lexer = new NumberLexer(numStr);
        var tokens = lexer.getTokens();

        var total = 0;
        int currentGroup = 0;

        for (var token : tokens) {
            switch (token.type) {
                case LITERAL -> currentGroup += token.value;
                case HUNDRED -> currentGroup *= token.value;
                case GROUP_BOUNDARY -> {
                    currentGroup *= token.value;
                    total += currentGroup;
                    currentGroup = 0;
                }
            }
        }

        return total + currentGroup;
    }
}
