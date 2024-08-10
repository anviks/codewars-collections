/*
 * https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
 */

const number = (num, func) => func === undefined ? num : func(num);

export const zero = func => number(0, func);
export const one = func => number(1, func);
export const two = func => number(2, func);
export const three = func => number(3, func);
export const four = func => number(4, func);
export const five = func => number(5, func);
export const six = func => number(6, func);
export const seven = func => number(7, func);
export const eight = func => number(8, func);
export const nine = func => number(9, func);

export const plus = num => a => a + num;
export const minus = num => a => a - num;
export const times = num => a => a * num;
export const dividedBy = num => a => Math.floor(a / num);
