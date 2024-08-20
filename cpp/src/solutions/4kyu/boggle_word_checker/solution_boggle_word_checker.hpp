#ifndef CODEWARS_CPP_SOLUTION_BOGGLE_WORD_CHECKER_HPP
#define CODEWARS_CPP_SOLUTION_BOGGLE_WORD_CHECKER_HPP

#include <vector>
#include <string>

using namespace std;
typedef pair<int, int> coord;

bool check_word(const vector<vector<char>>& board, const string& word, coord pos = coord(-1, -1));

#endif //CODEWARS_CPP_SOLUTION_BOGGLE_WORD_CHECKER_HPP