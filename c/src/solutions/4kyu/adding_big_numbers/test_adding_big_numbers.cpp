/*
 * https://www.codewars.com/kata/525f4206b73515bffb000b21
 */

extern "C" {
    #include "solution_adding_big_numbers.h"
}

#include "../../../test_macros.hpp"
#include <catch2/catch_all.hpp>

static void tester(const char* a, const char* b, const char* expected) {
    char* submitted = add(a, b);
    char buffer[200];
    snprintf(buffer, 200, "a = \"%s\"\nb = \"%s\"\nExpected:  \"%s\"\nSubmitted: \"%s\"", a, b, expected, submitted);
    REQUIRE_MSG(strcmp(submitted, expected) == 0, buffer);
    free(submitted);
}

TEST_CASE("Example_Tests:should_pass_all_the_tests_provided", "[Example_Tests]"){
    tester("1", "1", "2");
    tester("123", "456", "579");  // 123 + 456 == 579
    tester("888", "222", "1110");
    tester("1372", "69", "1441");
    tester("12", "456", "468");
    tester("101", "100", "201");
    tester("63829983432984289347293874", "90938498237058927340892374089", "91002328220491911630239667963");
}
