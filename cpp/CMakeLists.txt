cmake_minimum_required(VERSION 3.26)
project(codewars_cpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(codewars_cpp main.cpp
        solutions/6kyu/equal_sides_of_an_array/solution_equal_sides_of_an_array.cpp
        solutions/6kyu/equal_sides_of_an_array/solution_equal_sides_of_an_array.h
        solutions/5kyu/rgb_to_hex_conversion/solution_rgb_to_hex_conversion.cpp
        solutions/5kyu/rgb_to_hex_conversion/solution_rgb_to_hex_conversion.h)


# Add Igloo include directory
find_path(IGLOO_INCLUDE_DIRS "igloo/igloo_alt.h"
        PATHS ${CMAKE_SOURCE_DIR}/cmake-build-debug/igloo/src/igloo
        NO_DEFAULT_PATH)

if(NOT IGLOO_INCLUDE_DIRS)
    set(IGLOO_INCLUDE_DIRS "${CMAKE_SOURCE_DIR}/cmake-build-debug/igloo/src/igloo")
endif()

find_path(IGLOO_INCLUDE_DIRS "igloo/core/alternativeregistrationaliases.h")


# Create executable for tests
add_executable(tests test_main.cpp
        solutions/6kyu/equal_sides_of_an_array/test_equal_sides_of_an_array.cpp
        solutions/5kyu/rgb_to_hex_conversion/test_rgb_to_hex_conversion.cpp
)

# Include directories for the test executable
target_include_directories(tests PRIVATE ${IGLOO_INCLUDE_DIRS})
target_include_directories(tests PRIVATE ${CMAKE_SOURCE_DIR})

target_sources(tests PRIVATE
        solutions/6kyu/equal_sides_of_an_array/solution_equal_sides_of_an_array.cpp
        solutions/5kyu/rgb_to_hex_conversion/solution_rgb_to_hex_conversion.cpp)

## Add Igloo library
#add_library(igloo STATIC IMPORTED)
#set_target_properties(igloo PROPERTIES
#        IMPORTED_LOCATION ${CMAKE_SOURCE_DIR}/cmake-build-debug/igloo/src/igloo/igloo/igloo_framework.h)
#
## Link the test executable with Igloo
#target_link_libraries(tests PRIVATE igloo)



#find_package(Catch2 3 REQUIRED)
## These tests can use the Catch2-provided main
#add_executable(tests solutions/6kyu/equal_sides_of_an_array/test_equal_sides_of_an_array.cpp)
#target_link_libraries(tests PRIVATE Catch2::Catch2WithMain)
#
## These tests need their own main
#add_executable(custom-main-tests test.cpp test-main.cpp)
#target_link_libraries(custom-main-tests PRIVATE Catch2::Catch2)
