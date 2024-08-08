#include <iostream>
#include "7_kyu/sort_numbers.h"
#include "7_kyu/count_vowels.h"
#include "7_kyu/count_divisors.h"
#include "6_kyu/equal_array_sides.h"
#include "5_kyu/rgb_to_hex.h"
#include "4_kyu/boggle_word_checker.h"
#include "4_kyu/ranking_poker_hands.h"
#include "4_kyu/matrix_determinant.h"
#include "4_kyu/next_biggest_number.h"
#include "4_kyu/range_extraction.h"
#include <chrono>
#include <functional>

#define measure_time(action) \
    auto start = chrono::high_resolution_clock::now(); \
    auto result = action; \
    auto end = chrono::high_resolution_clock::now(); \
    chrono::duration<double, micro> duration = end - start; \
    cout << "Time taken: " << duration.count() / 1'000'000 << " seconds" << endl; \
    return result;

using namespace std;


struct Point {
    int x;
    int y;
};

bool operator==(const Point& first, const Point& second) {
    return first.x == second.x
           && first.y == second.y;
}

ostream& operator<<(ostream& stream, const Point& point) {
    return stream << "(" << point.x << ", " << point.y << ")";
}

void bubble_sort(int numbers[], size_t size) {
    bool flag = true;

    while (flag) {
        flag = false;

        for (int i = 1; i < size; i++) {
            if (numbers[i - 1] > numbers[i]) {
                swap(numbers[i - 1], numbers[i]);
                flag = true;
            }
        }
    }
}


int main() {
    test_range_extraction();
    
    return 0;
}
