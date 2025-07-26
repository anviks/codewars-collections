#include "criterion_wrapper.hpp"
#include <cstdarg>
#include <stdarg.h>
#include <string.h>
#include <string>
#include <vector>

std::string vformat(const char* fmt, va_list args) {
    va_list args_copy;
    va_copy(args_copy, args);
    int size = std::vsnprintf(nullptr, 0, fmt, args_copy);
    va_end(args_copy);

    if (size < 0) return "Format error";

    std::vector<char> buf(size + 1);
    std::vsnprintf(buf.data(), buf.size(), fmt, args);
    return std::string(buf.data(), size);
}

std::string assert_impl(const int condition, ...) {
    if (condition) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, condition);
    return msg;
}

std::string assert_not_impl(const int condition, ...) {
    if (!condition) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, condition);
    return msg;
}

std::string assert_str_eq_impl(const char* s1, const char* s2, ...) {
    if (strcmp(s1, s2) == 0) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, s2);
    return msg;
}
