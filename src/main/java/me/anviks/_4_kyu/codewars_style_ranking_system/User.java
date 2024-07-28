package me.anviks._4_kyu.codewars_style_ranking_system;

/*
 * https://www.codewars.com/kata/51fda2d95d6efda45e00004e
 */

public class User {
    public int progress;
    public int rank;

    public User() {
        rank = -8;
        progress = 0;
    }

    public void checkRankUp() {
        if (progress >= 100 && rank < 8) {
            if (rank != -1) {
                rank++;
            } else {
                rank += 2;
            }
            progress -= 100;
            checkRankUp();
        } else if (rank == 8) {
            progress = 0;
        }
    }

    public void incProgress(int activityRank) throws IllegalArgumentException {
        if (activityRank < -8 || activityRank == 0 || activityRank > 8) {
            throw new IllegalArgumentException();
        }
        if (activityRank == rank) {
            progress += 3;
        } else if (activityRank + 1 == rank || activityRank == -1 && rank == 1) {
            progress++;
        } else if (activityRank > rank) {
            int difference = activityRank - rank;
            if (activityRank > 0 && rank < 0) {
                difference -= 1;
            }
            progress += 10 * Math.pow(difference, 2);
        }
        checkRankUp();
    }
}