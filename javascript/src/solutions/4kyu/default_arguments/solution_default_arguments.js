/*
 * https://www.codewars.com/kata/52605419be184942d400003d
 */

const STRIP_COMMENTS = /((\/\/.*$)|(\/\*[\s\S]*?\*\/))/mg;
const ARGUMENT_NAMES = /([^\s,]+)/g;

const originalFunctions = new Map();

function getParameterNames(func) {
    const fnStr = func.toString().replace(STRIP_COMMENTS, '');
    return fnStr.slice(fnStr.indexOf('(') + 1, fnStr.indexOf(')')).match(ARGUMENT_NAMES);
}

export function defaultArguments(func, params) {
    while (originalFunctions.has(func)) {
        func = originalFunctions.get(func);
    }

    const paramNames = getParameterNames(func);

    let foo = (...args) => {
        for (let i = args.length; i < paramNames?.length ?? 0; i++) {
            if (params[paramNames[i]]) {
                args.push(params[paramNames[i]]);
            }
        }

        return func(...args);
    };

    originalFunctions.set(foo, func);

    return foo;
}
