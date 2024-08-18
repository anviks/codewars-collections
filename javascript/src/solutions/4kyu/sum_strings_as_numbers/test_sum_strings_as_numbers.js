/*
 * https://www.codewars.com/kata/5324945e2ece5e1f32000370
 */

import { sumStrings } from './solution_sum_strings_as_numbers.js';
import { assert } from 'chai';

describe('Tests', () => {
    it('test', () => {
        assert.equal(sumStrings('123', '456'), '579');
    });
});
