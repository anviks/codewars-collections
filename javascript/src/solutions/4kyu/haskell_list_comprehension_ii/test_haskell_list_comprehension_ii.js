/*
 * https://www.codewars.com/kata/53c8bcb1689f84238c000661
 */

import { ArrayComprehension } from './solution_haskell_list_comprehension_ii.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual
};


function isPrime(num) {
    if (num < 2) return false;
    var result = true;
    if (num !== 2) {
        if (num % 2 === 0) {
            result = false;
        } else {
            for (var x = 3; result && x <= Math.sqrt(num); x += 2) {
                if (num % x === 0) {
                    result = false;
                }
            }
        }
    }
    return result;
}

function sum(x, y) {
    return Number(x) + Number(y);
}

function sumDigits(num) {
    return String(num).split('').reduce(sum, 0);
}


function double(num) {
    return num * 2;
}

function arrayWrapper(num) {
    return [num];
}


function checkSumDigits(min, number) {
    return sumDigits(number) >= min;
}

function compose(f, g) {
    return function(x) {
        return f(g(x));
    };
}

function partial1(fn, param) {
    return function() {
        return fn.apply(null, [param].concat(Array.prototype.slice.call(arguments) || []));
    };
}

var limitSumDigits = function(min) {
    return partial1(checkSumDigits, min);
};

describe('ArrayComprehension tests', function() {

    it('Range tests', function() {
        Test.assertSimilar(ArrayComprehension({ generator: '1..5' }), [1, 2, 3, 4, 5]);
        Test.assertSimilar(ArrayComprehension({ generator: '1,4..12' }), [1, 4, 7, 10]);
        Test.assertSimilar(ArrayComprehension({ generator: '12,10..4' }), [12, 10, 8, 6, 4]);
    });

    it('Simple Filter test', function() {
        Test.assertSimilar(ArrayComprehension({
            generator: '1..20',
            filters: [isPrime]
        }), [2, 3, 5, 7, 11, 13, 17, 19]);
    });


    it('Simple Filter test', function() {
        Test.assertSimilar(ArrayComprehension({
            generator: '1..20',
            filters: [isPrime, limitSumDigits(5)]
        }), [5, 7, 17, 19]);
    });


    it('Simple Transform test', function() {
        Test.assertSimilar(ArrayComprehension({
            generator: '1,5,6,78,9,-3',
            transform: arrayWrapper
        }), [[1], [5], [6], [78], [9], [-3]]);
    });


    it('Compose Transform test', function() {
        Test.assertSimilar(ArrayComprehension({
            generator: '50..60',
            transform: compose(arrayWrapper, double)
        }), [[100], [102], [104], [106], [108], [110], [112], [114], [116], [118], [120]]);
    });


    it('All together test', function() {
        Test.assertSimilar(ArrayComprehension({
            generator: '1..20',
            filters: [isPrime, limitSumDigits(4)],
            transform: compose(arrayWrapper, double)
        }), [[10], [14], [26], [34], [38]]);

        Test.assertSimilar(ArrayComprehension({
            generator: '15,18..50',
            filters: [isPrime, limitSumDigits(4)],
            transform: compose(arrayWrapper, double)
        }), []);
    });


});
