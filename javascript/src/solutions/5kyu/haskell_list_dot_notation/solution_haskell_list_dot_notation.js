/*
 * https://www.codewars.com/kata/53c8b29750fe70e4a2000610
 */

export function ArrayComprehension(options) {
    let generator = options.generator;

    if (generator === undefined) {
        return [];
    } else if (!generator.includes('..')) {
        return generator.trim() ? generator.split(',').map(s => parseInt(s)) : [];
    } else if (!generator.includes(',')) {
        let nums = generator.split('..').map(s => parseInt(s));
        if (nums[0] > nums[1]) {
            return [];
        }
        return range(...nums);
    }

    let [first, rest] = generator.split(',');
    let [start, end] = rest.split('..').map(s => parseInt(s));
    first = parseInt(first);

    return range(first, end, start - first);
}

function range(start, end, step = 1) {
    let arr = [];

    let cmp = step < 0
        ? (a, b) => a >= b
        : (a, b) => a <= b;

    for (let i = start; cmp(i, end); i += step) {
        arr.push(i);
    }

    return arr;
}
