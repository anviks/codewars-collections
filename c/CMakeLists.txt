cmake_minimum_required(VERSION 3.22)
project(codewars_c)

set(CMAKE_C_STANDARD 23)
set(CMAKE_CXX_STANDARD 20)

find_package(GTest REQUIRED)

include_directories(${GTEST_INCLUDE_DIRS})

file(GLOB SOLUTION_SOURCES
        "src/solutions/*/*/solution_*.c"
        "src/solutions/*/*/preloaded.c"
)

file(GLOB TEST_SOURCES
        "src/solutions/*/*/test_*.cpp"
)

list(REMOVE_ITEM SOLUTION_SOURCES "${CMAKE_SOURCE_DIR}/src/solutions/4kyu/ordered_set/solution_ordered_set.c")
list(REMOVE_ITEM TEST_SOURCES "${CMAKE_SOURCE_DIR}/src/solutions/4kyu/ordered_set/test_ordered_set.cpp")

# Create an object library to compile solutions once
add_library(solutions OBJECT
        ${SOLUTION_SOURCES}
)

add_executable(codewars_c src/main.c $<TARGET_OBJECTS:solutions>)

# Create executable for tests
add_executable(tests
        src/test_main.cpp
        src/criterion_wrapper.cpp
        $<TARGET_OBJECTS:solutions>
        ${TEST_SOURCES}
)

target_include_directories(tests PRIVATE /usr/include)
target_link_libraries(tests PRIVATE ${GTEST_LIBRARIES} m)
