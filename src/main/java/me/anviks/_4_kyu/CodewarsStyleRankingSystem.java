package me.anviks._4_kyu;


/**
 * <a href="https://www.codewars.com/kata/51fda2d95d6efda45e00004e"><h2>Codewars style ranking system</h2></a>
 * <p>
 * Write a class called User that is used to calculate the amount that a user will progress through a ranking system similar to the one Codewars uses.
 * </p>
 * <p>
 * Business Rules:
 * </p>
 * <ul>
 * <li>A user starts at rank -8 and can progress all the way to 8.</li>
 * <li>There is no 0 (zero) rank. The next rank after -1 is 1.</li>
 * <li>Users will complete activities. These activities also have ranks.</li>
 * <li>Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank</li>
 * <li>The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity</li>
 * <li>A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level</li>
 * <li>Any remaining progress earned while in the previous rank will be applied towards the next rank's progress (we don't throw any progress away).</li>
 * <li>The exception is if there is no other rank left to progress towards (Once you reach rank 8 there is no more progression).</li>
 * <li>A user cannot progress beyond rank 8.</li>
 * <li>The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.</li>
 * </ul>
 * <p>
 * The progress is scored like so:
 * </p>
 * <ul>
 * <li>Completing an activity that is ranked the same as that of the user's will be worth 3 points</li>
 * <li>Completing an activity that is ranked one ranking lower than the user's will be worth 1 point</li>
 * <li>Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored</li>
 * <li>Completing an activity ranked higher than the current user's rank will accelerate the rank progression. The greater the difference between rankings the more the progression will be increased. The formula is <code>10 * d * d</code>, where <code>d</code> equals the difference in ranking between the activity and the user.</li>
 * </ul>
 * <p>
 * Logic Examples:
 * </p>
 * <ul>
 * <li>If a user ranked -8 completes an activity ranked -7 they will receive 10 progress</li>
 * <li>If a user ranked -8 completes an activity ranked -6 they will receive 40 progress</li>
 * <li>If a user ranked -8 completes an activity ranked -5 they will receive 90 progress</li>
 * <li>If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting in the user being upgraded to rank -7 and having earned 60 progress towards their next rank</li>
 * <li>If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)</li>
 * </ul>
 * <p>
 * Code Usage Examples:
 * </p>
 * <pre>
 * <code>
 * User user = new User();
 * user.rank; // => -8
 * user.progress; // => 0
 * user.incProgress(-7);
 * user.progress; // => 10
 * user.incProgress(-5); // will add 90 progress
 * user.progress; // => 0 // progress is now zero
 * user.rank; // => -7 // rank was upgraded to -7
 * </code>
 * </pre>
 * <p>
 * Note: In Java some methods may throw an IllegalArgumentException.
 * </p>
 * <p>
 * Note: Codewars no longer uses this algorithm for its own ranking system. It uses a pure Math based solution that gives consistent results no matter what order a set of ranked activities are completed at.
 */
public class CodewarsStyleRankingSystem {
    public static void main(String[] args) {
        User user = new User();
        user.incProgress(-8);
        user.incProgress(-8); // will add 90 progress
        System.out.println(user.rank);
        System.out.println(user.progress);

        user = new User();
        System.out.println(user.rank); // => -8
        System.out.println(user.progress); // => 0
        user.incProgress(-7);
        System.out.println(user.progress); // => 10
        user.incProgress(-5); // will add 90 progress
        System.out.println(user.progress); // => 0 // progress is now zero
        System.out.println(user.rank); // => -7 // rank was upgraded to -7
    }


    public static class User {

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
}
