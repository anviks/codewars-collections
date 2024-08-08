<?php

/*
 * https://www.codewars.com/kata/57f8ff867a28db569e000c4a
 */

use PHPUnit\Framework\TestCase;

require 'solution_kebabize.php';

class MyTests extends TestCase
{
    public function testIt()
    {
        $this->assertSame('my-camel-cased-string', kebabize('myCamelCasedString'));
        $this->assertSame('my-camel-has-humps', kebabize('myCamelHas3Humps'));
    }
}
