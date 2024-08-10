/*
 * https://www.codewars.com/kata/55ba24f1cb367c48ac0000a2
 */

export function CurryIt(func) {
    let allArgs = [];
    let context;

    function curried(...args) {
        if (!context) {
            context = this;
        }

        if (args.length === 0) {
            const tempArgs = allArgs;
            const result = func.call(context, ...tempArgs);
            allArgs = [];
            context = null;
            return result;
        } else {
            allArgs = allArgs.concat(args);
            return curried;
        }
    }

    return curried;
}
