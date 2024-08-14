/*
 * https://www.codewars.com/kata/52a382ee44408cea2500074c
 */

#include "solution_matrix_determinant.hpp"

#include <iostream>
#include <vector>

using namespace std;

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
