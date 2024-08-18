/*
 * https://www.codewars.com/kata/54ca3e777120b56cb6000710
 */

import { chained } from './solution_unary_function_chainer.js';
import { assert } from 'chai';

const { deepEqual } = assert;

describe('tests suite', function() {

    function doTest(functions, arg, expected) {
        const actual = chained(functions)(arg);
        deepEqual(actual, expected);
    }

    it('sample tests', function() {
        function f1(x) {
            return x * 2;
        }

        function f2(x) {
            return x + 2;
        }

        function f3(x) {
            return Math.pow(x, 2);
        }

        function f4(x) {
            return x.split('').concat().reverse().join('').split(' ');
        }

        function f5(xs) {
            return xs.concat().reverse();
        }

        function f6(xs) {
            return xs.join('_');
        }

        // functions,      arg,    expected
        doTest([f1, f2, f3], 0, 4);
        doTest([f1, f2, f3], 2, 36);
        doTest([f3, f2, f1], 2, 12);
        doTest([f4, f5, f6], 'lorem ipsum', 'merol_muspi');
    });
});
