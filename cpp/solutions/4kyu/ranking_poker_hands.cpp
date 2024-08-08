//
// Created by Andreas Viks on 09.06.2024.
//
// https://www.codewars.com/kata/5739174624fc28e188000465
//

#include <cassert>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <functional>
#include "ranking_poker_hands.h"

using namespace std;

struct PokerHand {
    int cards[5][2]{};
    set<int> unique_values = {};
    set<int> unique_suits = {};
    vector<int> sorted_values = {};

    explicit PokerHand(const char* pokerhand) {
        for (int i = 0; i < 5; i++) {
            switch (pokerhand[i * 3]) {
                case 'T':
                    cards[i][0] = 10;
                    break;
                case 'J':
                    cards[i][0] = 11;
                    break;
                case 'Q':
                    cards[i][0] = 12;
                    break;
                case 'K':
                    cards[i][0] = 13;
                    break;
                case 'A':
                    cards[i][0] = 14;
                    break;
                default:
                    cards[i][0] = pokerhand[i * 3] - '0';
                    break;
            }

            switch (pokerhand[i * 3 + 1]) {
                case 'S':
                    cards[i][1] = 0;
                    break;
                case 'H':
                    cards[i][1] = 1;
                    break;
                case 'D':
                    cards[i][1] = 2;
                    break;
                case 'C':
                    cards[i][1] = 3;
                    break;
            }
        }

        for (auto& card: cards) {
            unique_suits.insert(card[1]);
            unique_values.insert(card[0]);
            sorted_values.push_back(card[0]);
        }

        sort(sorted_values.begin(), sorted_values.end());
    }

    [[nodiscard]] bool has_straight_flush() const {
        return has_straight() && has_flush();
    }

    [[nodiscard]] bool has_four_of_a_kind() const {
        if (unique_values.size() != 2) return false;

        for (auto value: unique_values) {
            if (count(sorted_values.begin(), sorted_values.end(), value) == 4) return true;
        }

        return false;
    }

    [[nodiscard]] bool has_full_house() const {
        return has_pair() && has_three_of_a_kind();
    }

    [[nodiscard]] bool has_flush() const {
        return unique_suits.size() == 1;
    }

    [[nodiscard]] bool has_straight() const {
        return unique_values.size() == 5 && (*unique_values.rbegin() - *unique_values.begin()) == 4;
    }
    
    [[nodiscard]] bool has_low_ace_straight() const {
        return unique_values.size() == 5 && *unique_values.rbegin() == 14 && sorted_values[3] - sorted_values[0] == 3;
    }

    [[nodiscard]] bool has_three_of_a_kind() const {
        for (auto value: unique_values) {
            if (count(sorted_values.begin(), sorted_values.end(), value) == 3) return true;
        }

        return false;
    }

    [[nodiscard]] bool has_two_pairs() const {
        int pairs = 0;
        for (auto value: unique_values) {
            if (count(sorted_values.begin(), sorted_values.end(), value) == 2) pairs++;
        }

        return pairs == 2;
    }

    [[nodiscard]] bool has_pair() const {
        for (auto value: unique_values) {
            if (count(sorted_values.begin(), sorted_values.end(), value) == 2) return true;
        }

        return false;
    }
};

enum class Result {
    Win, Loss, Tie
};

Result compare_values(const std::vector<int>& player_values, const std::vector<int>& opponent_values) {
    for (int i = 4; i >= 0; i--) {
        if (player_values[i] > opponent_values[i]) return Result::Win;
        if (player_values[i] < opponent_values[i]) return Result::Loss;
    }
    return Result::Tie;
}

Result compare_hands(bool player_has_hand, bool opponent_has_hand, const std::vector<int>& player_values, const std::vector<int>& opponent_values) {
    if (player_has_hand && !opponent_has_hand) return Result::Win;
    if (!player_has_hand && opponent_has_hand) return Result::Loss;
    if (player_has_hand && opponent_has_hand) {
        return compare_values(player_values, opponent_values);
    }
    return Result::Tie;
}

Result compare(const PokerHand& player, const PokerHand& opponent) {
    vector<function<Result()>> comparisons = {
            [&]() { return compare_hands(player.has_straight_flush(), opponent.has_straight_flush(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_four_of_a_kind(), opponent.has_four_of_a_kind(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_full_house(), opponent.has_full_house(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_flush(), opponent.has_flush(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_straight(), opponent.has_straight(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_low_ace_straight(), opponent.has_low_ace_straight(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_three_of_a_kind(), opponent.has_three_of_a_kind(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_two_pairs(), opponent.has_two_pairs(), player.sorted_values, opponent.sorted_values); },
            [&]() { return compare_hands(player.has_pair(), opponent.has_pair(), player.sorted_values, opponent.sorted_values); }
    };

    for (const auto& compare_func : comparisons) {
        Result result = compare_func();
        if (result != Result::Tie) {
            return result;
        }
    }

    return compare_values(player.sorted_values, opponent.sorted_values);
}

void test_ranking_poker_hands() {
    assert(compare(PokerHand("2H 3H 4H 5H 6H"), PokerHand("KS AS TS QS JS")) ==
           Result::Loss);  // "Highest straight flush wins"
    assert(compare(PokerHand("2H 3H 4H 5H 6H"), PokerHand("AS AD AC AH JD")) ==
           Result::Win);  // "Straight flush wins of 4 of a kind"
    assert(compare(PokerHand("AS AH 2H AD AC"), PokerHand("JS JD JC JH 3D")) ==
           Result::Win);  // "Highest 4 of a kind wins"
    assert(compare(PokerHand("2S AH 2H AS AC"), PokerHand("JS JD JC JH AD")) ==
           Result::Loss);  // "4 Of a kind wins of full house"
    assert(compare(PokerHand("2S AH 2H AS AC"), PokerHand("2H 3H 5H 6H 7H")) ==
           Result::Win);  // "Full house wins of flush"
    assert(compare(PokerHand("AS 3S 4S 8S 2S"), PokerHand("2H 3H 5H 6H 7H")) == Result::Win);  // "Highest flush wins"
    assert(compare(PokerHand("2H 3H 5H 6H 7H"), PokerHand("2S 3H 4H 5S 6C")) ==
           Result::Win);  // "Flush wins of straight"
    assert(compare(PokerHand("2S 3H 4H 5S 6C"), PokerHand("3D 4C 5H 6H 2S")) ==
           Result::Tie);  // "Equal straight is tie"
    assert(compare(PokerHand("2S 3H 4H 5S 6C"), PokerHand("AH AC 5H 6H AS")) ==
           Result::Win);  // "Straight wins of three of a kind"
    assert(compare(PokerHand("2S 3H 4H 5S AC"), PokerHand("AH AC 5H 6H AS")) ==
           Result::Win);  // "Low-ace straight wins of three of a kind"
    assert(compare(PokerHand("2S 2H 4H 5S 4C"), PokerHand("AH AC 5H 6H AS")) ==
           Result::Loss);  // "3 Of a kind wins of two pair"
    assert(compare(PokerHand("2S 2H 4H 5S 4C"), PokerHand("AH AC 5H 6H 7S")) == Result::Win);  // "2 Pair wins of pair"
    assert(compare(PokerHand("6S AD 7H 4S AS"), PokerHand("AH AC 5H 6H 7S")) == Result::Loss);  // "Highest pair wins"
    assert(compare(PokerHand("2S AH 4H 5S KC"), PokerHand("AH AC 5H 6H 7S")) ==
           Result::Loss);  // "Pair wins of nothing"
    assert(compare(PokerHand("2S 3H 6H 7S 9C"), PokerHand("7H 3C TH 6H 9S")) == Result::Loss);  // "Highest card loses"
    assert(compare(PokerHand("4S 5H 6H TS AC"), PokerHand("3S 5H 6H TS AC")) == Result::Win);  // "Highest card wins"
    assert(compare(PokerHand("2S AH 4H 5S 6C"), PokerHand("AD 4C 5H 6H 2C")) == Result::Tie);  // "Equal cards is tie"

    assert(compare(PokerHand("3C 5C 4C 2C AH"), PokerHand("JS QS 9H TS KH")) == Result::Loss);  // "Flush wins of straight"
    
    assert(compare(PokerHand("4C 4H 6S 3S 2C"), PokerHand("3C 3H 9H TS KH")) == Result::Win);  // "Highest pair wins"
}
    