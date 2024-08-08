<?php

/*
 * https://www.codewars.com/kata/57f8ff867a28db569e000c4a
 */

function kebabize($string): array|string|null
{
    $kebabCase = preg_replace_callback('/([A-Z])/m', function ($matches) {
        return '-' . strtolower($matches[1]);
    }, $string);
    return trim(preg_replace('/[^a-z-]/', '', $kebabCase), '-');
}
