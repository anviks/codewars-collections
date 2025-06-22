/*
 * https://www.codewars.com/kata/52c4dd683bfd3b434c000292
 */

package me.anviks.codewars.solutions._4kyu.catching_car_mileage_numbers;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CarMileageTest {

  @Test 
  public void testTooSmall() {
    assertEquals(0, CarMileage.isInteresting(3, new int[]{1337, 256}));
  }
  
  @Test 
  public void testAlmostAwesome() {
    assertEquals(1, CarMileage.isInteresting(1336, new int[]{1337, 256}));
  }
  
  @Test 
  public void testAwesome() {
    assertEquals(2, CarMileage.isInteresting(1337, new int[]{1337, 256}));
  }
  
  @Test 
  public void testFarNotInteresting() {
    assertEquals(0, CarMileage.isInteresting(11208, new int[]{1337, 256}));
  }
  
  @Test 
  public void testAlmostInteresting() {
    assertEquals(1, CarMileage.isInteresting(11209, new int[]{1337, 256}));
  }
  
  @Test 
  public void testInteresting() {
    assertEquals(2, CarMileage.isInteresting(11211, new int[]{1337, 256}));
  }
  
}
