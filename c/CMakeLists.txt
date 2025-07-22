cmake_minimum_required(VERSION 3.22)
project(codewars_c)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 20)

# Create an object library to compile solutions once
add_library(solutions OBJECT
        src/solutions/4kyu/adding_big_numbers/solution_adding_big_numbers.c
        src/solutions/4kyu/multiplying_numbers_as_strings/solution_multiplying_numbers_as_strings.c
        src/solutions/4kyu/sort_binary_tree_by_levels/solution_sort_binary_tree_by_levels.c
        src/solutions/6kyu/is_a_number_prime/solution_is_a_number_prime.c
        src/solutions/6kyu/n_th_fibonacci/solution_n_th_fibonacci.c
        src/solutions/6kyu/new_cashier_does_not_know_about_space_or_shift/solution_new_cashier_does_not_know_about_space_or_shift.c
        src/solutions/6kyu/next_smaller_pronic/solution_next_smaller_pronic.c
        src/solutions/6kyu/reverse_every_other_word_in_the_string/solution_reverse_every_other_word_in_the_string.c
)

add_executable(codewars_c src/main.c $<TARGET_OBJECTS:solutions>)

# Create executable for tests
add_executable(tests src/test_main.c
        $<TARGET_OBJECTS:solutions>
        src/solutions/4kyu/adding_big_numbers/test_adding_big_numbers.c
        src/solutions/4kyu/multiplying_numbers_as_strings/test_multiplying_numbers_as_strings.c
        src/solutions/4kyu/sort_binary_tree_by_levels/test_sort_binary_tree_by_levels.c
        src/solutions/6kyu/is_a_number_prime/test_is_a_number_prime.c
        src/solutions/6kyu/n_th_fibonacci/test_n_th_fibonacci.c
        src/solutions/6kyu/new_cashier_does_not_know_about_space_or_shift/test_new_cashier_does_not_know_about_space_or_shift.c
        src/solutions/6kyu/next_smaller_pronic/test_next_smaller_pronic.c
        src/solutions/6kyu/reverse_every_other_word_in_the_string/test_reverse_every_other_word_in_the_string.c
)

target_include_directories(tests PRIVATE /usr/include)
target_link_libraries(tests PRIVATE criterion m)
