/*
 * https://www.codewars.com/kata/5886e082a836a691340000c3
 */

extern "C" {
#include "solution_simple_fun_number_27_rectangle_rotation.h"
}

#include "../../../criterion_wrapper.hpp"

Test(solution_test, basic_tests) {
    cr_assert_eq(rectangle_rotation(6, 4), 23);
    cr_assert_eq(rectangle_rotation(30, 2), 65);
    cr_assert_eq(rectangle_rotation(8, 6), 49);
    cr_assert_eq(rectangle_rotation(16, 20), 333);
}
