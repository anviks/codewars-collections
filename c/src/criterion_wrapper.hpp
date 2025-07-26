#ifndef CRITERION_WRAPPER_H
#define CRITERION_WRAPPER_H

#include <cstddef>
#include <gmock/gmock.h>
#include <gtest/gtest.h>
#include <stdarg.h>
#include <string>

std::string vformat(const char* fmt, va_list args);

#define FORMAT_VARARGS_TO(output_var, last_param)                                                                      \
    va_list _args;                                                                                                     \
    va_start(_args, last_param);                                                                                       \
    const char* _fmt = va_arg(_args, const char*);                                                                     \
    std::string output_var;                                                                                            \
    if (!_fmt || _fmt[0] == '\0') {                                                                                    \
        output_var = "Invalid format string";                                                                          \
    } else {                                                                                                           \
        output_var = vformat(_fmt, _args);                                                                             \
    }                                                                                                                  \
    va_end(_args);

std::string assert_impl(const bool condition, ...);

std::string assert_not_impl(const bool condition, ...);

template <typename T> std::string assert_eq_impl(T val1, T val2, ...) {
    if (val1 == val2) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, val2);
    return msg;
}

std::string assert_str_eq_impl(const char* s1, const char* s2, ...);

template <typename T> std::string assert_arr_eq_impl(const T* arr1, const T* arr2, size_t count, ...) {
    for (size_t i = 0; i < count; ++i) {
        if (arr1[i] != arr2[i]) {
            FORMAT_VARARGS_TO(msg, count);
            return msg;
        }
    }
    return "";  // Success
}

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

#define cr_assert_arr_eq(arr1, arr2, nb_bytes, ...)                                                                    \
    do {                                                                                                               \
        using ElemType = typename std::remove_reference<decltype(*arr1)>::type;                                        \
        size_t _count = (nb_bytes) / sizeof(ElemType);                                                                 \
        int vararg_count = std::tuple_size<decltype(std::make_tuple(__VA_ARGS__))>::value;                             \
        if (vararg_count == 0) {                                                                                       \
            ASSERT_THAT(std::vector<ElemType>(actual, actual + _count),                                                \
                        ::testing::ElementsAreArray(expected, _count));                                                \
        } else {                                                                                                       \
            std::string _msg = assert_arr_eq_impl(arr1, arr2, _count, ##__VA_ARGS__);                                  \
            if (!_msg.empty()) {                                                                                       \
                FAIL() << _msg;                                                                                        \
            }                                                                                                          \
        }                                                                                                              \
    } while (0)

#endif  // CRITERION_WRAPPER_H
