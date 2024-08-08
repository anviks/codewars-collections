//
// Created by Andreas Viks on 30.05.2024.
//

#include "boggle_word_checker.h"
#include <vector>
#include <string>
#include <complex>
#include <set>
#include <cassert>
#include <utility>

using namespace std;

typedef pair<int, int> coord;

bool check_word(const vector<vector<char>> &board, const string &word) {
    set<coord> visited;
    
    
    
    return false;
}

void test_boggle() {
    vector<vector<char> > test_board = {
            {'E', 'A', 'R', 'A'},
            {'N', 'L', 'E', 'C'},
            {'I', 'A', 'I', 'S'},
            {'B', 'Y', 'O', 'R'}
    };

    assert(check_word(test_board, "C") == true);
    assert(check_word(test_board, "EAR") == true);
    assert(check_word(test_board, "EARS") == false);
    assert(check_word(test_board, "BAILER") == true);
    assert(check_word(test_board, "RSCAREIOYBAILNEA") == true); // Must be able to check indefinite word lengths going in all directions
    assert(check_word(test_board, "CEREAL") == false); // Valid guesses can't overlap themselves
    assert(check_word(test_board, "ROBES") == false); // Valid guesses have to be adjacent
    assert(check_word(test_board, "BAKER") == false); // All the letters have to be in the board
    assert(check_word(test_board, "CARS") == false); // Valid guesses cannot wrap around the edges of the board
}
