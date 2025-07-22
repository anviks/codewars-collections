/*
 * https://www.codewars.com/kata/525f4206b73515bffb000b21
 */

#include "solution_adding_big_numbers.h"

#include <criterion/criterion.h>
#include <stdlib.h>
#include <string.h>

char *add(const char *a, const char *b);
static void tester(const char *ta, const char *tb, const char *expected);

Test(add, Sample_Tests)
{
    tester(    "1",   "1",    "2" );
    tester(  "123", "456",  "579" );  // 123 + 456 == 579
    tester(  "888", "222", "1110" );
    tester( "1372",  "69", "1441" );
    tester(   "12", "456",  "468" );
    tester(  "101", "100",  "201" );
    tester(    "63829983432984289347293874",
            "90938498237058927340892374089",
            "91002328220491911630239667963" );
}

static void tester(const char *a, const char *b, const char *expected) {
    char *submitted = add(a, b);
    cr_assert_str_eq(                                        submitted,         expected,
        "< Incorrect Result >\n \na = \"%s\"\nb = \"%s\"\n \nSubmitted: \"%s\"\nExpected:  \"%s\"",
                                  a,          b,             submitted,         expected);
    free(submitted);
    submitted = NULL;
}
