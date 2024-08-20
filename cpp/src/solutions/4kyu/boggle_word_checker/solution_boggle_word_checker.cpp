/*
 * https://www.codewars.com/kata/57680d0128ed87c94f000bfd
 */

#include "solution_boggle_word_checker.hpp"
#include <vector>
#include <string>

using namespace std;

typedef pair<int, int> coord;

bool check_word(const vector<vector<char>>& board, const string& word, coord pos) {
    if (word.empty()) return true;
    
    if (pos.first == -1) {
        for (int i = 0; i < board.size(); i++) {
            for (int j = 0; j < board[i].size(); j++) {
                if (board[i][j] == word[0]) {
                    auto new_board = board;
                    new_board[i][j] = '#';
                    if (check_word(new_board, word.substr(1), coord(i, j))) {
                        return true;
                    }
                }
            }
        }
    } else {
        for (int i = -1; i < 2; i++) {
            auto new_row = pos.first + i;
            if (new_row < 0 || new_row >= board.size()) continue;
            
            for (int j = -1; j < 2; j++) {
                auto new_col = pos.second + j;
                if (new_col < 0 || new_col >= board[0].size()) continue;
                
                if (board[new_row][new_col] == word[0]) {
                    auto new_board = board;
                    new_board[new_row][new_col] = '#';
                    if (check_word(new_board, word.substr(1), coord(new_row, new_col))) {
                        return true;
                    }
                }
            }
        }
    }

    return false;
}
