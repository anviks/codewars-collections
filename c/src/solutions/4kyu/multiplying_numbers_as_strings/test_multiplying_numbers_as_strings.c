/*
 * https://www.codewars.com/kata/55911ef14065454c75000062
 */

#include "solution_multiplying_numbers_as_strings.h"

#include <stdlib.h>
#include <criterion/criterion.h>

static void do_test (const char *a, const char *b, const char *axb);

Test(the_multiply_function, should_pass_some_simple_assertions) {
  do_test("2", "3", "6");
  do_test("30", "69", "2070");
  do_test("11", "85", "935");
}

Test(the_multiply_function, should_pass_some_edge_assertions) {
  do_test("2", "0", "0");
  do_test("0", "30", "0");
  do_test("0000001", "3", "3");
  do_test("1009", "03", "3027");
}

Test(the_multiply_function, should_pass_some_advanced_fixed_assertions) {
  do_test("98765", "56894", "5619135910");
  do_test("1020303004875647366210", "2774537626200857473632627613", "2830869077153280552556547081187254342445169156730");
  do_test("58608473622772837728372827", "7586374672263726736374", "444625839871840560024489175424316205566214109298");
  do_test("9007199254740991", "9007199254740991", "81129638414606663681390495662081");
}

extern char *multiply(const char *, const char *);

static void do_test (const char *a, const char *b, const char *axb)
{
  char *actual = multiply(a, b);
  cr_assert_str_eq(actual, axb,
    "a = \"%s\"\nb = \"%s\"\na * b = \"%s\"\nbut got \"%s\"",
    a, b, axb, actual
  );
  free(actual);
}
