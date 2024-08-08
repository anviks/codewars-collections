<?php

function stripComments(string $str, array $markers): string
{
    $markers = preg_quote(implode('', $markers), '/');
    return $markers 
        ? preg_replace("/[ \t]*[$markers].*/", '', $str) ?? $str 
        : $str;
}
