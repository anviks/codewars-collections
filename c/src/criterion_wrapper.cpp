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
    
template <typename T1, typename T2> std::string assert_eq_impl(T1 val1, T2 val2, ...) {
    if (val1 == val2) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, val2);
    return msg;
}

std::string assert_str_eq_impl(const char* s1, const char* s2, ...) {
    if (strcmp(s1, s2) == 0) {
        return "";  // Success
    }

    FORMAT_VARARGS_TO(msg, s2);
    return msg;
}
