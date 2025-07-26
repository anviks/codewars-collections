/*
 * https://www.codewars.com/kata/58d76854024c72c3e20000de
 */

extern "C" {
#include "solution_reverse_every_other_word_in_the_string.h"
}

#include "../../../criterion_wrapper.hpp"
#include <stdlib.h>
#include <string.h>

void reverse_alternate(const char *string, char *result);
static void tester(const char *string, const char *expected);

Test(reverse_alternate, Sample_Tests) {
    tester("Did it work?", "Did ti work?");
    tester("I really hope it works this time...", "I yllaer hope ti works siht time...");
    tester("Reverse this string, please!", "Reverse siht string, !esaelp");
    tester("Have a beer", "Have a beer");
    tester("   ", "");
}

static void tester(const char *string, const char *expected) {
	size_t length = strlen(string);
    char* submitted = new char[length + 1];
	memset(submitted, '@', length + 1);
    reverse_alternate(string, submitted);
    cr_assert_str_eq(submitted, expected,
      "< Incorrect Result >\n \nstring  =  \"%s\"\n \nSubmitted: \"%s\"\nExpected:  \"%s\"\n \n",
                                string,               submitted,         expected
    );
    delete[] submitted;
}
