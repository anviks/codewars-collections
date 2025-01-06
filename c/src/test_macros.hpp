#ifndef CODEWARS_C_TEST_MACROS_HPP
#define CODEWARS_C_TEST_MACROS_HPP

#define REQUIRE_MSG(expr, msg) INFO(msg); REQUIRE(expr);
#define REQUIRE_FALSE_MSG(expr, msg) INFO(msg); REQUIRE_FALSE(expr);
#define CHECK_MSG(expr, msg) INFO(msg); CHECK(expr);
#define CHECK_FALSE_MSG(expr, msg) INFO(msg); CHECK_FALSE(expr);

#endif //CODEWARS_C_TEST_MACROS_HPP
