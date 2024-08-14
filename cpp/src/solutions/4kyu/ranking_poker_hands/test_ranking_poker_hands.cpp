/*
 * https://www.codewars.com/kata/5739174624fc28e188000465
 */

#include "solution_ranking_poker_hands.hpp"

#include <catch2/catch_all.hpp>

Result compare(const PokerHand& player, const PokerHand& opponent);

bool run_test_hands(const PokerHand& player, const PokerHand& opponent, Result outcome) {
    return outcome == compare(player, opponent);
}

bool run_test(const char* player, const char* opponent, Result outcome) {
    return run_test_hands(PokerHand(player), PokerHand(opponent), outcome);
}

TEST_CASE("compare_poker_hands") {
    SECTION("should_pass_all_the_tests_provided") {
        REQUIRE(run_test("2H 3H 4H 5H 6H", "KS AS TS QS JS", Result::Loss)); // "Highest straight flush wins"
        REQUIRE(run_test("2H 3H 4H 5H 6H", "AS AD AC AH JD", Result::Win)); // "Straight flush wins of 4 of a kind"
        REQUIRE(run_test("AS AH 2H AD AC", "JS JD JC JH 3D", Result::Win)); // "Highest 4 of a kind wins"
        REQUIRE(run_test("2S AH 2H AS AC", "JS JD JC JH AD", Result::Loss)); // "4 Of a kind wins of full house"
        REQUIRE(run_test("2S AH 2H AS AC", "2H 3H 5H 6H 7H", Result::Win)); // "Full house wins of flush"
        REQUIRE(run_test("AS 3S 4S 8S 2S", "2H 3H 5H 6H 7H", Result::Win)); // "Highest flush wins"
        REQUIRE(run_test("2H 3H 5H 6H 7H", "2S 3H 4H 5S 6C", Result::Win)); // "Flush wins of straight"
        REQUIRE(run_test("2S 3H 4H 5S 6C", "3D 4C 5H 6H 2S", Result::Tie)); // "Equal straight is tie"
        REQUIRE(run_test("2S 3H 4H 5S 6C", "AH AC 5H 6H AS", Result::Win)); // "Straight wins of three of a kind"
        REQUIRE(run_test("2S 3H 4H 5S AC", "AH AC 5H 6H AS",
                         Result::Win)); // "Low-ace straight wins of three of a kind"
        REQUIRE(run_test("2S 2H 4H 5S 4C", "AH AC 5H 6H AS", Result::Loss)); // "3 Of a kind wins of two pair"
        REQUIRE(run_test("2S 2H 4H 5S 4C", "AH AC 5H 6H 7S", Result::Win)); // "2 Pair wins of pair"
        REQUIRE(run_test("6S AD 7H 4S AS", "AH AC 5H 6H 7S", Result::Loss)); // "Highest pair wins"
        REQUIRE(run_test("2S AH 4H 5S KC", "AH AC 5H 6H 7S", Result::Loss)); // "Pair wins of nothing"
        REQUIRE(run_test("2S 3H 6H 7S 9C", "7H 3C TH 6H 9S", Result::Loss)); // "Highest card loses"
        REQUIRE(run_test("4S 5H 6H TS AC", "3S 5H 6H TS AC", Result::Win)); // "Highest card wins"
        REQUIRE(run_test("2S AH 4H 5S 6C", "AD 4C 5H 6H 2C", Result::Tie)); // "Equal cards is tie"
    }
}
