/*
 * https://www.codewars.com/kata/5ac739ed3fdf73d3f0000048
 */

const True = T => F => T;
const False = T => F => F;

export const Not = A => A(False)(True);
export const And = A => B => A(B)(A)
export const Or = A => B => Not(And(Not(A))(Not(B)))
export const Xor = A => B => And(Or(A)(B))(Not(And(A)(B)))
