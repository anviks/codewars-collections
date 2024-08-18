/*
 * https://www.codewars.com/kata/5655c60db4c2ce0c2e000026
 */

import { compose } from './solution_function_composition.js';
import { assert } from 'chai';

const addOne = (a) => a + 1;
const multTwo = (b) => b * 2;

describe('Function composition', () => {
    it('example tests', () => {
        assert.strictEqual(compose(multTwo, addOne)(5), 12, 'compose two functions');
        assert.strictEqual(compose(addOne, multTwo, addOne, addOne)(2), 9, 'compose four functions');
        assert.strictEqual(compose(addOne)(3), 4, 'compose one function');
        assert.strictEqual(compose()(10), 10, 'compose no functions');
    });
});
