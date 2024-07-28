package me.anviks._6_kyu.sum_of_digits_digital_root;

/*
 * https://www.codewars.com/kata/541c8630095125aba6000c00
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class DRootExampleTest {
    @Test
    public void Test1() {
      assertEquals( "Nope!" , 7, DRoot.digital_root(16));
    }      
    @Test
    public void Test2() {
      assertEquals( "Nope!" , 6, DRoot.digital_root(456));
    }
}
