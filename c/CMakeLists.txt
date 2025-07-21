cmake_minimum_required(VERSION 3.24)
project(codewars_c)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 20)

set(Catch2_DIR vcpkg_installed/x64-windows/share/Catch2)

# Find the Catch2 package
find_package(Catch2 3 REQUIRED)

# Create an object library to compile solutions once
add_library(solutions OBJECT
        src/solutions/6kyu/is_a_number_prime/solution_is_a_number_prime.c
        src/solutions/6kyu/next_smaller_pronic/solution_next_smaller_pronic.c
        src/solutions/6kyu/reverse_every_other_word_in_the_string/solution_reverse_every_other_word_in_the_string.c
        src/solutions/6kyu/n_th_fibonacci/solution_n_th_fibonacci.c
        src/solutions/4kyu/adding_big_numbers/solution_adding_big_numbers.c
        src/solutions/6kyu/new_cashier_does_not_know_about_space_or_shift/solution_new_cashier_does_not_know_about_space_or_shift.c
        src/solutions/4kyu/multiplying_numbers_as_strings/solution_multiplying_numbers_as_strings.c
)

add_executable(codewars_c src/main.c $<TARGET_OBJECTS:solutions>)

# Create executable for tests
add_executable(tests src/test_main.cpp
        $<TARGET_OBJECTS:solutions>
        src/solutions/6kyu/is_a_number_prime/test_is_a_number_prime.cpp
        src/solutions/6kyu/next_smaller_pronic/test_next_smaller_pronic.cpp
        src/solutions/6kyu/reverse_every_other_word_in_the_string/test_reverse_every_other_word_in_the_string.cpp
        src/solutions/4kyu/adding_big_numbers/test_adding_big_numbers.cpp
        src/solutions/6kyu/new_cashier_does_not_know_about_space_or_shift/test_new_cashier_does_not_know_about_space_or_shift.cpp
        src/solutions/4kyu/multiplying_numbers_as_strings/test_multiplying_numbers_as_strings.cpp
)

target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
