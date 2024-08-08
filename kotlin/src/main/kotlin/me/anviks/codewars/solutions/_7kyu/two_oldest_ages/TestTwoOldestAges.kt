/*
 * https://www.codewars.com/kata/511f11d355fe575d2c000001
 */

package me.anviks.codewars.solutions._7kyu.two_oldest_ages

import io.kotlintest.matchers.shouldBe
import io.kotlintest.specs.StringSpec

class TestTwoOldestAges : StringSpec() {
    init {
        "twoOldestAges(listOf(1,5,87,45,8,8)) should be listOf(45, 87)" {
            twoOldestAges(listOf(1, 5, 87, 45, 8, 8)) shouldBe listOf(45, 87)
        }
        "twoOldestAges(listOf(6,5,83,5,3,18)) should be listOf(18, 83)" {
            twoOldestAges(listOf(6, 5, 83, 5, 3, 18)) shouldBe listOf(18, 83)
        }
    }
}
