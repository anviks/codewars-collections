/*
 * https://www.codewars.com/kata/5655c60db4c2ce0c2e000026
 */

export function compose(...funcs) {
    return (arg) => {
        funcs.reverse().forEach(fn => arg = fn(arg));
        return arg;
    };
}
