/*
 * https://www.codewars.com/kata/58d76854024c72c3e20000de
 */

extern "C" {
#include "solution_reverse_every_other_word_in_the_string.h"
}

#include "../../../test_macros.hpp"
#include <catch2/catch_all.hpp>


#include <stdlib.h>
#include <string.h>


static void tester(const char* string, const char* expected);

TEST_CASE("reverse_alternate:Sample_Tests", "[reverse_alternate]") {
    tester("Did it work?", "Did ti work?");
    tester("I really hope it works this time...", "I yllaer hope ti works siht time...");
    tester("Reverse this string, please!", "Reverse siht string, !esaelp");
    tester("Have a beer", "Have a beer");
    tester("   ", "");
    tester("This       is a  test ", "This si a tset");
    tester("  jc4Ng.eS     Ngd7!ivBs 0bi?9UCuBHux?QNByFT7 nfzZFDpoHIEKV0L e9CDRBSCS34BLg", "jc4Ng.eS sBvi!7dgN 0bi?9UCuBHux?QNByFT7 L0VKEIHopDFZzfn e9CDRBSCS34BLg");
}

static void tester(const char* string, const char* expected) {
    const size_t length = strlen(string);
    std::vector submitted(length + 1, '@');
    reverse_alternate(string, submitted.data());
    char buffer[200];
    snprintf(buffer, 200, "< Incorrect Result >\n \nstring  =  \"%s\"\n \nSubmitted: \"%s\"\nExpected:  \"%s\"\n \n",
             string, submitted.data(), expected);
    REQUIRE_MSG(!strcmp(submitted.data(), expected), buffer);
}
