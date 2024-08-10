/*
 * https://www.codewars.com/kata/54ca3e777120b56cb6000710
 */

export function chained(functions) {
    return (arg) => {
        functions.forEach(fn => arg = fn(arg));
        return arg;
    };
}
