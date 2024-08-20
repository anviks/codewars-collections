<?php

/*
 * https://www.codewars.com/kata/58223370aef9fc03fd000071
 */

use PHPUnit\Framework\TestCase;

require 'solution_dashatize_it.php';


class DashatizeItTest extends TestCase
{
    public function testBasic() {
        $this->assertSame('2-7-4', dashatize(274));
        $this->assertSame('5-3-1-1', dashatize(5311));
        $this->assertSame('86-3-20', dashatize(86320));
        $this->assertSame('9-7-4-3-02', dashatize(974302));
    }

    public function testWeird() {
        $this->assertSame('0', dashatize(0));
        $this->assertSame('1', dashatize(-1));
        $this->assertSame('28-3-6-9', dashatize(-28369));
    }
}
