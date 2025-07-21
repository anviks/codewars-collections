#ifndef CODEWARS_C_TEST_MACROS_HPP
#define CODEWARS_C_TEST_MACROS_HPP

#define REQUIRE_MSG(expr, msg)                                                                                         \
    INFO(msg);                                                                                                         \
    REQUIRE(expr);

#define REQUIRE_FALSE_MSG(expr, msg)                                                                                   \
    INFO(msg);                                                                                                         \
    REQUIRE_FALSE(expr);

#define CHECK_MSG(expr, msg)                                                                                           \
    INFO(msg);                                                                                                         \
    CHECK(expr);

#define CHECK_FALSE_MSG(expr, msg)                                                                                     \
    INFO(msg);                                                                                                         \
    CHECK_FALSE(expr);

#define REQUIRE_STR_EQ(str1, str2)                                                                                     \
    INFO("Comparing strings: \"" << str1 << "\" and \"" << str2 << "\"");                                              \
    REQUIRE(strcmp(str1, str2) == 0);

#endif  // CODEWARS_C_TEST_MACROS_HPP
