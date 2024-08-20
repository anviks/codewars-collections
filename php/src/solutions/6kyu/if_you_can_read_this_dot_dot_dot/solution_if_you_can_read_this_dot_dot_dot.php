<?php

/*
 * https://www.codewars.com/kata/586538146b56991861000293
 */


function to_nato($words): string
{
    $NATO = [
        'A' => 'Alfa',
        'B' => 'Bravo',
        'C' => 'Charlie',
        'D' => 'Delta',
        'E' => 'Echo',
        'F' => 'Foxtrot',
        'G' => 'Golf',
        'H' => 'Hotel',
        'I' => 'India',
        'J' => 'Juliett',
        'K' => 'Kilo',
        'L' => 'Lima',
        'M' => 'Mike',
        'N' => 'November',
        'O' => 'Oscar',
        'P' => 'Papa',
        'Q' => 'Quebec',
        'R' => 'Romeo',
        'S' => 'Sierra',
        'T' => 'Tango',
        'U' => 'Uniform',
        'V' => 'Victor',
        'W' => 'Whiskey',
        'X' => 'Xray',
        'Y' => 'Yankee',
        'Z' => 'Zulu',
    ];

    
    $result = '';

    foreach (str_split($words) as $char) {
        $result .= ($NATO[strtoupper($char)] ?? $char) . ' ';
    }

    return preg_replace('/ +/', ' ', trim($result));
}
