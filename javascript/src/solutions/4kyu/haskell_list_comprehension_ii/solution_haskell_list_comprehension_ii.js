/*
 * https://www.codewars.com/kata/53c8bcb1689f84238c000661
 */

export function ArrayComprehension(options) {
    let generator = options.generator;
    let filters = options.filters;
    let transform = options.transform;

    let items;

    if (generator === undefined) {
        return [];
    } else if (!generator.includes('..')) {
        items = generator.trim() ? generator.split(',').map(s => parseInt(s)) : [];
    } else if (!generator.includes(',')) {
        let nums = generator.split('..').map(s => parseInt(s));
        if (nums[0] > nums[1]) {
            return [];
        }
        items = range(...nums);
    } else {
        let [first, rest] = generator.split(',');
        let [start, end] = rest.split('..').map(s => parseInt(s));
        first = parseInt(first);
        items = range(first, end, start - first);
    }

    if (filters !== undefined) {
        filters.forEach(f => items = items.filter(f));
    }

    if (transform !== undefined) {
        items = items.map(transform);
    }

    return items;
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

//Filter
function isPrime(num) {
    if (num > 2) {
        if (num % 2 === 0) {
            return false;
        } else {
            for (let x = 3; x <= Math.sqrt(num); x += 2) {
                if (num % x === 0) {
                    return false;
                }
            }
        }
    } else return num === 2;

    return true;
}

//Transform
function arrayWrapper(num) {
    return [num];
}

let result = ArrayComprehension({
    generator: "1..50",
    filters: [isPrime],
    transform: arrayWrapper
}); // returns [[2], [3], [5], [7], [11], [13], [17], [19], [23], [29], [31], [37], [41], [43], [47]]

