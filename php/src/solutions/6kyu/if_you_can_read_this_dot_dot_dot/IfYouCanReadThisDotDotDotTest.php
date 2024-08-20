<?php

/*
 * https://www.codewars.com/kata/586538146b56991861000293
 */

use PHPUnit\Framework\TestCase;

require 'solution_if_you_can_read_this_dot_dot_dot.php';


class IfYouCanReadThisDotDotDotTest extends TestCase
{
    public function testShouldReturnTranslatedString() {
      $this->assertSame("India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta", to_nato('If you can read'));
      $this->assertSame("Delta India Delta November Oscar Tango Sierra Echo Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf", to_nato('Did not see that coming'));
    }
}
