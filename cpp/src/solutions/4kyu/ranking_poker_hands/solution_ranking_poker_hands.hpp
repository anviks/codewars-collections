#ifndef CODEWARS_CPP_SOLUTION_RANKING_POKER_HANDS_HPP
#define CODEWARS_CPP_SOLUTION_RANKING_POKER_HANDS_HPP

#include <set>
#include <vector>

struct PokerHand {
    int cards[5][2]{};
    std::set<int> unique_values = {};
    std::set<int> unique_suits = {};
    std::vector<int> sorted_values = {};

    explicit PokerHand(const char* pokerhand);

    [[nodiscard]] bool has_straight_flush() const;

    [[nodiscard]] bool has_four_of_a_kind() const;

    [[nodiscard]] bool has_full_house() const;

    [[nodiscard]] bool has_flush() const;

    [[nodiscard]] bool has_straight() const;

    [[nodiscard]] bool has_low_ace_straight() const;

    [[nodiscard]] bool has_three_of_a_kind() const;

    [[nodiscard]] bool has_two_pairs() const;

    [[nodiscard]] bool has_pair() const;
};

enum class Result {
    Win, Loss, Tie
};

#endif //CODEWARS_CPP_SOLUTION_RANKING_POKER_HANDS_HPP