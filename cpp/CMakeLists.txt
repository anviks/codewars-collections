cmake_minimum_required(VERSION 3.26)
project(codewars_cpp)

set(CMAKE_CXX_STANDARD 17)

set(Catch2_DIR vcpkg_installed/x64-windows/share/Catch2)

# Find the Catch2 package
find_package(Catch2 3 REQUIRED)

# Create an object library to compile solutions once
add_library(solutions OBJECT
        src/solutions/6kyu/equal_sides_of_an_array/solution_equal_sides_of_an_array.cpp
        src/solutions/5kyu/rgb_to_hex_conversion/solution_rgb_to_hex_conversion.cpp
        src/solutions/4kyu/boggle_word_checker/solution_boggle_word_checker.cpp
        src/solutions/4kyu/matrix_determinant/solution_matrix_determinant.cpp
        src/solutions/4kyu/next_bigger_number_with_the_same_digits/solution_next_bigger_number_with_the_same_digits.cpp
        src/solutions/4kyu/range_extraction/solution_range_extraction.cpp
        src/solutions/4kyu/ranking_poker_hands/solution_ranking_poker_hands.cpp
        src/solutions/7kyu/count_the_divisors_of_a_number/solution_count_the_divisors_of_a_number.cpp
        src/solutions/7kyu/vowel_count/solution_vowel_count.cpp
        src/solutions/7kyu/sort_numbers/solution_sort_numbers.cpp
)

add_executable(codewars_cpp main.cpp $<TARGET_OBJECTS:solutions>)

# Create executable for tests
add_executable(tests test_main.cpp
        $<TARGET_OBJECTS:solutions>
        solutions/6kyu/equal_sides_of_an_array/test_equal_sides_of_an_array.cpp
        solutions/5kyu/rgb_to_hex_conversion/test_rgb_to_hex_conversion.cpp
        solutions/4kyu/boggle_word_checker/test_boggle_word_checker.cpp
        solutions/4kyu/matrix_determinant/test_matrix_determinant.cpp
        solutions/4kyu/next_bigger_number_with_the_same_digits/test_next_bigger_number_with_the_same_digits.cpp
        solutions/4kyu/range_extraction/test_range_extraction.cpp
        solutions/4kyu/ranking_poker_hands/test_ranking_poker_hands.cpp
        solutions/7kyu/count_the_divisors_of_a_number/test_count_the_divisors_of_a_number.cpp
        solutions/7kyu/vowel_count/test_vowel_count.cpp
        solutions/7kyu/sort_numbers/test_sort_numbers.cpp
)

target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
