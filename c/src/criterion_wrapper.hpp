#ifndef CRITERION_WRAPPER_H
#define CRITERION_WRAPPER_H

#include <gtest/gtest.h>
#include <gmock/gmock.h>
#include <string>

std::string assert_impl(const bool condition, ...);

std::string assert_not_impl(const bool condition, ...);

template <typename T1, typename T2> std::string assert_eq_impl(T1 val1, T2 val2, ...);

std::string assert_str_eq_impl(const char* s1, const char* s2, ...);

// We'll use these macros to emulate Criterion's tests and assertions.

#define Test(suite_name, test_name) TEST(suite_name, test_name)

#define cr_assert(condition, ...)                                                                                      \
    do {                                                                                                               \
        int vararg_count = std::tuple_size<decltype(std::make_tuple(__VA_ARGS__))>::value;                             \
        if (vararg_count == 0) {                                                                                       \
            ASSERT_TRUE(condition);                                                                                    \
        } else {                                                                                                       \
            std::string _msg = assert_impl(condition, ##__VA_ARGS__);                                                  \
            if (!_msg.empty()) {                                                                                       \
                FAIL() << _msg;                                                                                        \
            }                                                                                                          \
        }                                                                                                              \
    } while (0)

#define cr_assert_not(condition, ...)                                                                                  \
    do {                                                                                                               \
        int vararg_count = std::tuple_size<decltype(std::make_tuple(__VA_ARGS__))>::value;                             \
        if (vararg_count == 0) {                                                                                       \
            ASSERT_FALSE(condition);                                                                                   \
        } else {                                                                                                       \
            std::string _msg = assert_not_impl(condition, ##__VA_ARGS__);                                              \
            if (!_msg.empty()) {                                                                                       \
                FAIL() << _msg;                                                                                        \
            }                                                                                                          \
        }                                                                                                              \
    } while (0)

#define cr_assert_eq(val1, val2, ...)                                                                                  \
    do {                                                                                                               \
        int vararg_count = std::tuple_size<decltype(std::make_tuple(__VA_ARGS__))>::value;                             \
        if (vararg_count == 0) {                                                                                       \
            ASSERT_EQ(val1, val2);                                                                                     \
        } else {                                                                                                       \
            std::string _msg = assert_eq_impl(val1, val2, ##__VA_ARGS__);                                              \
            if (!_msg.empty()) {                                                                                       \
                FAIL() << _msg;                                                                                        \
            }                                                                                                          \
        }                                                                                                              \
    } while (0)

#define cr_assert_str_eq(s1, s2, ...)                                                                                  \
    do {                                                                                                               \
        int vararg_count = std::tuple_size<decltype(std::make_tuple(__VA_ARGS__))>::value;                             \
        if (vararg_count == 0) {                                                                                       \
            ASSERT_STREQ(s1, s2);                                                                                      \
        } else {                                                                                                       \
            std::string _msg = assert_str_eq_impl(s1, s2, ##__VA_ARGS__);                                              \
            if (!_msg.empty()) {                                                                                       \
                FAIL() << _msg;                                                                                        \
            }                                                                                                          \
        }                                                                                                              \
    } while (0)


#endif  // CRITERION_WRAPPER_H
