/*
 * https://www.codewars.com/kata/5d23d89906f92a00267bb83d
 */

extern "C" {
#include "solution_new_cashier_does_not_know_about_space_or_shift.h"
}

#include "../../../criterion_wrapper.hpp"

char* get_order(const char* input);

Test(Sample_Cases, should_pass_all_the_tests_provided) {
    {
        const char* order_up = "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza";
        const char* expected = "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke";
        cr_assert_str_eq(get_order(order_up), expected);
    }
    {
        const char* order_up = "pizzachickenfriesburgercokemilkshakefriessandwich";
        const char* expected = "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke";
        cr_assert_str_eq(get_order(order_up), expected);
    }
}
