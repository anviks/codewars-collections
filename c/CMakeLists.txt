cmake_minimum_required(VERSION 3.24)
project(codewars_c C)

set(CMAKE_C_STANDARD 23)

add_executable(codewars_c main.c 6_kyu/is_prime.c 6_kyu/is_prime.h)
