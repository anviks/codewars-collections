cmake_minimum_required(VERSION 3.26)
project(codewars_cpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(codewars_cpp main.cpp
        solutions/7kyu/sort_numbers.cpp
        solutions/7kyu/count_vowels.cpp
        solutions/7kyu/count_vowels.h
        solutions/7kyu/count_vowels.cpp
        solutions/7kyu/count_divisors.cpp
        solutions/7kyu/count_divisors.h
        solutions/6kyu/equal_array_sides.cpp
        solutions/6kyu/equal_array_sides.h
        solutions/5kyu/rgb_to_hex.cpp
        solutions/5kyu/rgb_to_hex.h
        solutions/4kyu/boggle_word_checker.cpp
        solutions/4kyu/boggle_word_checker.h
        solutions/4kyu/ranking_poker_hands.cpp
        solutions/4kyu/ranking_poker_hands.h
        solutions/4kyu/matrix_determinant.cpp
        solutions/4kyu/matrix_determinant.h
        solutions/4kyu/next_biggest_number.cpp
        solutions/4kyu/next_biggest_number.h
        solutions/4kyu/range_extraction.cpp
        solutions/4kyu/range_extraction.h)
