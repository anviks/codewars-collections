/*
 * https://www.codewars.com/kata/53cf7e37e9876c35a60002c9
 */

export function curryPartial(fn, ...args) {
    if (fn.length <= args.length) {
        return fn(...args)
    }

    return (...x) => curryPartial(fn, ...args, ...x);
}
