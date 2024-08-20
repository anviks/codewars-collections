<?php

use PHPUnit\Framework\TestCase;

require 'solution_strip_comments.php';


class StripCommentsTest extends TestCase
{
    public function testShouldReturnStringWithoutComments()
    {
        $this->assertSame("apples, pears\ngrapes\nbananas", stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", ['#', '!']));
        $this->assertSame("a\nc\nd", stripComments("a #b\nc\nd \$e f g", ['#', '$']));
        $this->assertSame("apples, pears\ngrapes\nbananas", stripComments("apples, pears # and bananas\ngrapes\nbananas !#apples", ['#', '!']));
        $this->assertSame("apples, pears\ngrapes\nbananas", stripComments("apples, pears # and bananas\ngrapes\nbananas #!apples", ['#', '!']));
        $this->assertSame("apples, pears # and bananas\ngrapes\navocado", stripComments("apples, pears # and bananas\ngrapes\navocado @apples", ['@', '!']));
        $this->assertSame("apples, pears\ngrapes\navocado", stripComments("apples, pears § and bananas\ngrapes\navocado *apples", ['*', '§']));
        $this->assertSame("\tapples, pears\ngrapes\navocado", stripComments("\tapples, pears § and bananas\ngrapes\navocado *apples", ['*', '§']));
        $this->assertSame("  apples, pears\ngrapes\navocado", stripComments("  apples, pears § and bananas\ngrapes\navocado *apples", ['*', '§']));
        $this->assertSame("", stripComments("", ['#', '!']));
        $this->assertSame("", stripComments("#", ['#', '!']));
        $this->assertSame("\n", stripComments("\n§", ['#', '§']));
        $this->assertSame("apples, pears # and bananas\ngrapes\nbananas !apples", stripComments("apples, pears # and bananas\ngrapes\nbananas !apples", []));
    }

    private function solution($str, $markers): string
    {
        $markers = preg_quote(implode('', $markers), '/');
        return $markers
            ? preg_replace("/[ \t]*[$markers].*/", '', $str) ?? $str
            : $str;
    }

    private function generateRandomString(array $symbols, array $fruits): string
    {
        $testString = '';
        $symbolsCount = count($symbols);
        $fruitsCount = count($fruits);
        
        for ($i = 0; $i < rand(3, 5); $i++) {
            $line = '';
            for ($j = 0; $j < rand(1, 6); $j++) {
                if (rand(1, 13) < 9) {
                    $line .= $fruits[rand(0, $fruitsCount - 1)];
                } else {
                    $line .= $symbols[rand(0, $symbolsCount - 1)];
                }
                $line .= ' ';
            }
            $testString .= $line . PHP_EOL;
        }
        
        return $testString;
    }

    public function testRandomTests()
    {
        $symbols = ['@', '#', '!', '?', '\'', '^', '.', ',', '=', '-'];
        $fruits = ['avocados', 'pears', 'apples', 'bananas', 'cherries', 'strawberries', 'oranges', 'lemons', 'watermelons'];
        
        for ($i = 0; $i < 10; $i++) {
            shuffle($symbols);
            $testString = $this->generateRandomString($symbols, $fruits);
            $markers = array_slice($symbols, 0, rand(0, count($symbols) - 1));
            
            $this->assertSame($this->solution($testString, $markers), stripComments($testString, $markers));
        }
    }
}