/*
 * https://www.codewars.com/kata/513e08acc600c94f01000001
 */

#include <igloo/igloo_alt.h>
#include "solution_rgb_to_hex_conversion.h"

using namespace igloo;

Describe(ExampleTests) {
    It(BasicTests) {
        Assert::That(rgb_to_hex(0, 0, 0), Equals("000000"));
        Assert::That(rgb_to_hex(1, 2, 3), Equals("010203"));
        Assert::That(rgb_to_hex(255, 255, 255), Equals("FFFFFF"));
        Assert::That(rgb_to_hex(254, 253, 252), Equals("FEFDFC"));
        Assert::That(rgb_to_hex(-20, 275, 125), Equals("00FF7D"));
    }
};
