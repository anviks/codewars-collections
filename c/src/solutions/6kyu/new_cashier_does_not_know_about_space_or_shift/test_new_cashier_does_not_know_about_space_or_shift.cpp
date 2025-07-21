/*
 * https://www.codewars.com/kata/5d23d89906f92a00267bb83d
 */

extern "C" {
#include "solution_new_cashier_does_not_know_about_space_or_shift.h"
}

#include "../../../test_macros.hpp"
#include <catch2/catch_all.hpp>

TEST_CASE("Sample_Cases:should_pass_all_the_tests_provided", "[Sample_Cases]") {
    {
        const char* order_up = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza";
        const char* expected = "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke";
        REQUIRE_STR_EQ(get_order(order_up), expected);
    }
    {
        const char* order_up = "pizzachickenfriesburgercokemilkshakefriessandwich";
        const char* expected = "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke";
        REQUIRE_STR_EQ(get_order(order_up), expected);
    }
}
