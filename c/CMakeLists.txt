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
)

add_executable(codewars_c src/main.c $<TARGET_OBJECTS:solutions>)

# Create executable for tests
add_executable(tests src/test_main.cpp
        $<TARGET_OBJECTS:solutions>
        src/solutions/6kyu/is_a_number_prime/test_is_a_number_prime.cpp
)

target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
