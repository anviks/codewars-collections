/*
 * https://www.codewars.com/kata/5672682212c8ecf83e000050
 */

package me.anviks.codewars.solutions._4kyu.twice_linear


import org.junit.Test
import kotlin.test.assertEquals

class DblLinearMainTest {
  @Test
  fun test() {
    println("Fixed Tests dblLinear")
    testing(dblLinear(10), 22)
    testing(dblLinear(20), 57)
    testing(dblLinear(30), 91)
    
  }
  companion object {
    private fun testing(actual:Int, expected:Int) {
      assertEquals(expected.toLong(), actual.toLong())
    }
  }
}

