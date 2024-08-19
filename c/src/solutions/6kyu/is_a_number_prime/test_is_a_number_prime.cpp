/*
 * https://www.codewars.com/kata/5262119038c0985a5b00029f
 */

extern "C" {
    #include "solution_is_a_number_prime.h"
}

#include "../../../test_macros.hpp"

#include <catch2/catch_all.hpp>


TEST_CASE("Sample_Test:basic_test", "[Sample_Test]")
{
    REQUIRE_MSG(!is_prime(0), "Your solution returned that 0 is prime, but it's not");
    REQUIRE_MSG(!is_prime(1), "Your solution returned that 1 is prime, but it's not");
    REQUIRE_MSG(is_prime(2), "Your solution returned that 2 is not prime, but it is");
    REQUIRE_MSG(is_prime(73), "Your solution returned that 73 is not prime, but it is");
    REQUIRE_MSG(!is_prime(75), "Your solution returned that 75 is prime, but it's not");
    REQUIRE_MSG(!is_prime(-1), "Your solution returned that -1 is prime, but it's not");
}

TEST_CASE("Sample_Test:test_prime", "[Sample_Test]")
{
    REQUIRE_MSG(is_prime(3), "Your solution returned that 3 is not prime, but it is");
    REQUIRE_MSG(is_prime(5), "Your solution returned that 5 is not prime, but it is");
    REQUIRE_MSG(is_prime(7), "Your solution returned that 7 is not prime, but it is");
    REQUIRE_MSG(is_prime(41), "Your solution returned that 41 is not prime, but it is");
    REQUIRE_MSG(is_prime(5099), "Your solution returned that 5099 is not prime, but it is");
}

TEST_CASE("Sample_Test:test_not_prime", "[Sample_Test]")
{
    REQUIRE_MSG(!is_prime(4), "Your solution returned that 4 is prime, but it's not");
    REQUIRE_MSG(!is_prime(6), "Your solution returned that 6 is prime, but it's not");
    REQUIRE_MSG(!is_prime(8), "Your solution returned that 8 is prime, but it's not");
    REQUIRE_MSG(!is_prime(9), "Your solution returned that 9 is prime, but it's not");
    REQUIRE_MSG(!is_prime(45), "Your solution returned that 45 is prime, but it's not");
    REQUIRE_MSG(!is_prime(-5), "Your solution returned that -5 is prime, but it's not");
    REQUIRE_MSG(!is_prime(-8), "Your solution returned that -8 is prime, but it's not");
    REQUIRE_MSG(!is_prime(-41), "Your solution returned that -41 is prime, but it's not");
}

TEST_CASE("Sample_Test:test_large", "[Sample_Test]")
{
    REQUIRE_MSG(!is_prime(247464361), "Your solution returned that 247464361 is prime, but it's not");
    REQUIRE_MSG(is_prime(1634300119), "Your solution returned that 1634300119 is not prime, but it is");
}
