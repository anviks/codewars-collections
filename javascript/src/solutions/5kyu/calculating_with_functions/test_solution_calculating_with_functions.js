/*
 * https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
 */

import {
    zero,
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    plus,
    minus,
    times,
    dividedBy
} from './solution_calculating_with_functions.js';
import { assert } from 'chai';

describe('Tests', () => {
    it('test', () => {
        assert.strictEqual(seven(times(five())), 35);
        assert.strictEqual(four(plus(nine())), 13);
        assert.strictEqual(eight(minus(three())), 5);
        assert.strictEqual(six(dividedBy(two())), 3);
    });
});

