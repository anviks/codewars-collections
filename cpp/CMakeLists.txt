cmake_minimum_required(VERSION 3.26)
project(codewars_c__)

set(CMAKE_CXX_STANDARD 17)

add_executable(codewars_c__ main.cpp
        7_kyu/sort_numbers.cpp
        7_kyu/count_vowels.cpp
        7_kyu/count_vowels.h
        7_kyu/count_vowels.cpp
        7_kyu/count_divisors.cpp
        7_kyu/count_divisors.h
        6_kyu/equal_array_sides.cpp
        6_kyu/equal_array_sides.h
        5_kyu/rgb_to_hex.cpp
        5_kyu/rgb_to_hex.h
        4_kyu/boggle_word_checker.cpp
        4_kyu/boggle_word_checker.h
        4_kyu/ranking_poker_hands.cpp
        4_kyu/ranking_poker_hands.h
        4_kyu/matrix_determinant.cpp
        4_kyu/matrix_determinant.h
        4_kyu/next_biggest_number.cpp
        4_kyu/next_biggest_number.h
        4_kyu/range_extraction.cpp
        4_kyu/range_extraction.h)
