<?php

/*
 * https://www.codewars.com/kata/58223370aef9fc03fd000071
 */

function dashatize(int $num): string
{
    $num = abs($num);
    $chars = ['-'];

    foreach (str_split(strval($num)) as $item) {
        if ($item % 2 == 1) {
            if ($chars[sizeof($chars) - 1] != '-') {
                $chars[] = '-';
            }
            $chars[] = $item;
            $chars[] = '-';
        } else {
            $chars[] = $item;
        }
    }
    
    unset($chars[0]);
    if ($num % 2 == 1) unset($chars[sizeof($chars)]);
    
    return implode($chars);
}
