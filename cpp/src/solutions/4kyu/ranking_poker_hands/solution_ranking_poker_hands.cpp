/*
 * https://www.codewars.com/kata/5739174624fc28e188000465
 */

#include "solution_ranking_poker_hands.hpp"

#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

PokerHand::PokerHand(const char* pokerhand) {
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

bool PokerHand::has_straight_flush() const {
    return has_straight() && has_flush();
}

bool PokerHand::has_four_of_a_kind() const {
    if (unique_values.size() != 2) return false;

    for (auto value: unique_values) {
        if (count(sorted_values.begin(), sorted_values.end(), value) == 4) return true;
    }

    return false;
}

bool PokerHand::has_full_house() const {
    return has_pair() && has_three_of_a_kind();
}

bool PokerHand::has_flush() const {
    return unique_suits.size() == 1;
}

bool PokerHand::has_straight() const {
    return unique_values.size() == 5 && (*unique_values.rbegin() - *unique_values.begin()) == 4;
}

bool PokerHand::has_low_ace_straight() const {
    return unique_values.size() == 5 && *unique_values.rbegin() == 14 && sorted_values[3] - sorted_values[0] == 3;
}

bool PokerHand::has_three_of_a_kind() const {
    return any_of(unique_values.begin(), unique_values.end(), [&](int value) {
        return count(sorted_values.begin(), sorted_values.end(), value) == 3;
    });
}

bool PokerHand::has_two_pairs() const {
    int pairs = 0;
    
    for (auto value: unique_values) {
        if (count(sorted_values.begin(), sorted_values.end(), value) == 2) pairs++;
    }

    return pairs == 2;
}

bool PokerHand::has_pair() const {
    return any_of(unique_values.begin(), unique_values.end(), [&](int value) {
        return count(sorted_values.begin(), sorted_values.end(), value) == 2;
    });
}

Result compare_values(const std::vector<int>& player_values, const std::vector<int>& opponent_values) {
    for (int i = 4; i >= 0; i--) {
        if (player_values[i] > opponent_values[i]) return Result::Win;
        if (player_values[i] < opponent_values[i]) return Result::Loss;
    }
    return Result::Tie;
}

Result compare_hands(bool player_has_hand, bool opponent_has_hand, const std::vector<int>& player_values,
                     const std::vector<int>& opponent_values) {
    if (player_has_hand && !opponent_has_hand) return Result::Win;
    if (!player_has_hand && opponent_has_hand) return Result::Loss;
    if (player_has_hand && opponent_has_hand) {
        return compare_values(player_values, opponent_values);
    }
    return Result::Tie;
}

Result compare(const PokerHand& player, const PokerHand& opponent) {
    vector<function<Result()>> comparisons = {
            [&]() {
                return compare_hands(player.has_straight_flush(), opponent.has_straight_flush(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_four_of_a_kind(), opponent.has_four_of_a_kind(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_full_house(), opponent.has_full_house(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_flush(), opponent.has_flush(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_straight(), opponent.has_straight(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_low_ace_straight(), opponent.has_low_ace_straight(),
                                     player.sorted_values, opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_three_of_a_kind(), opponent.has_three_of_a_kind(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_two_pairs(), opponent.has_two_pairs(), player.sorted_values,
                                     opponent.sorted_values);
            },
            [&]() {
                return compare_hands(player.has_pair(), opponent.has_pair(), player.sorted_values,
                                     opponent.sorted_values);
            }
    };

    for (const auto& compare_func: comparisons) {
        Result result = compare_func();
        if (result != Result::Tie) {
            return result;
        }
    }

    return compare_values(player.sorted_values, opponent.sorted_values);
}
