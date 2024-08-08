//
// Created by Andreas Viks on 10.06.2024.
// https://www.codewars.com/kata/52a382ee44408cea2500074c
//

#include <iostream>
#include <vector>
#include <chrono>
#include "matrix_determinant.h"

using namespace std;

//long long determinant(vector<vector<long long>> matrix) {
//    if (matrix.empty()) {
//        return 0;
//    }
//
//    if (matrix.size() == 1) {
//        return matrix[0][0];
//    }
//    
//    if (matrix.size() == 2) {
//        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
//    }
//
//    long long o = 0;
//
//    for (int i = 0; i < matrix.size(); i++) {
//        long long u = 1;
//        for (int j = 0; j < matrix.size(); j++) {
//            unsigned int column = (j + i) % matrix.size();
//            u *= matrix[j][column];
//        }
//        o += u;
//    }
//
//    for (int i = 0; i < matrix.size(); i++) {
//        long long u = 1;
//        for (int j = 0; j < matrix.size(); j++) {
//            unsigned int column = matrix.size() - 1 - ((j + i) % matrix.size());
//            u *= matrix[j][column];
//        }
//        o -= u;
//    }
//    
//    return o;
//}

long long determinant(vector<vector<long long>> matrix) {
    if (matrix.empty()) {
        return 0;
    }

    if (matrix.size() == 1) {
        return matrix[0][0];
    }

    if (matrix.size() == 2) {
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];
    }

    long long det = 0;

    for (int i = 0; i < matrix.size(); i++) {
        vector<vector<long long>> n_minor;

        for (int j = 1; j < matrix.size(); j++) {
            n_minor.emplace_back();
            for (int k = 0; k < matrix.size(); k++) {
                if (k == i) continue;
                n_minor.back().push_back(matrix[j][k]);
            }
        }

        long long n = matrix[0][i];
        long long result = n * determinant(n_minor);

        if (i % 2 == 0) {
            det += result;
        } else {
            det -= result;
        }
    }

    return det;
}

void test_matrix_determinant() {
    auto start_time = chrono::high_resolution_clock::now();
    
    vector<vector<long long>> matrix = {
            {1, 3},
            {2, 5}
    };
    cout << determinant(matrix) << endl;  // 1*5 - 3*2 = -1

    matrix = {
            {2, 5,  3},
            {1, -2, -1},
            {1, 3,  4}
    };
    cout << determinant(matrix) << endl;  // 2*(-2*4 - -1*3) - 5*(1*4 - -1*1) + 3*(1*3 - -2*1) = -20

    matrix = {
            {1}
    };
    cout << determinant(matrix) << endl;  // 1

    matrix = {
            {1, 2, 3, 4},
            {5, 0, 2, 8},
            {3, 5, 6, 7},
            {2, 5, 3, 1}
    };
    cout << determinant(matrix) << endl;  // 24

    matrix = {
            {-8, 9,  -6, 8,  -8},
            {2,  -6, 9,  1,  -8},
            {-4, 7,  -9, 4,  -4},
            {6,  -4, -3, -7, -10},
            {-2, 5,  4,  -6, 6}
    };
    cout << determinant(matrix) << endl;  // -10964

    matrix = {
            {10, 10, 1,  -5,  -5,  9,  -10},
            {9,  7,  -3, -5,  -8,  -6, -6},
            {10, 10, -7, 10,  -1,  1,  -9},
            {5,  5,  4,  8,   -10, 9,  10},
            {7,  -9, -2, 4,   10,  9,  7},
            {-6, 6,  8,  -10, 2,   -8, -6},
            {5,  -4, -2, 2,   -5,  1,  1}
    };
    cout << determinant(matrix) << endl;  // 36109134

    matrix = {
            {7,  -3, -5,  -8,  -6, -6},
            {10, -7, 10,  -1,  1,  -9},
            {5,  4,  8,   -10, 9,  10},
            {-9, -2, 4,   10,  9,  7},
            {6,  8,  -10, 2,   -8, -6},
            {-4, -2, 2,   -5,  1,  1}
    };
    cout << determinant(matrix) << endl;  // -424102

    matrix = {
            {-7, 10,  -1,  1,  -9},
            {4,  8,   -10, 9,  10},
            {-2, 4,   10,  9,  7},
            {8,  -10, 2,   -8, -6},
            {-2, 2,   -5,  1,  1}
    };
    cout << determinant(matrix) << endl;  // -18938
    
    matrix = {
            {8,  -10, 9,  10},
            {4,  10,  9,  7},
            {-10, 2,  -8, -6},
            {2,  -5, 1,  1}
    };
    cout << determinant(matrix) << endl;  // -422

    matrix = {
            {10, 9,  7},
            {2,  -8, -6},
            {-5, 1,  1}
    };
    cout << determinant(matrix) << endl;  // -34
    
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double, micro> duration = end_time - start_time;
    cout << "Time taken: " << duration.count() / 1'000'000 << " seconds" << std::endl;
}
