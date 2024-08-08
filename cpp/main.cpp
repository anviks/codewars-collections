#include <iostream>
#include "solutions/7kyu/sort_numbers.h"
#include "solutions/7kyu/count_vowels.h"
#include "solutions/7kyu/count_divisors.h"
#include "solutions/6kyu/equal_array_sides.h"
#include "solutions/5kyu/rgb_to_hex.h"
#include "solutions/4kyu/boggle_word_checker.h"
#include "solutions/4kyu/ranking_poker_hands.h"
#include "solutions/4kyu/matrix_determinant.h"
#include "solutions/4kyu/next_biggest_number.h"
#include "solutions/4kyu/range_extraction.h"
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
