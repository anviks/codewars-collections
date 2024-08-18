/*
 * https://www.codewars.com/kata/5ac739ed3fdf73d3f0000048
 */

import { And, Not, Or, Xor } from './solution_church_booleans.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    expect: assert.isTrue,
    expectError: (message, fn) => assert.throws(fn, null, null, message)
};

describe('Simple tests', () => {
    it('Not', () => {
        Test.assertEquals(unchurch(Not(True)), false, 'Not(True) is False');
    });
    it('And', () => {
        Test.assertEquals(unchurch(And(True)(True)), true, 'And(True)(True) is True');
        Test.assertEquals(unchurch(And(True)(False)), false, 'And(True)(False) is False');
    });
    it('Or', () => {
        Test.assertEquals(unchurch(Or(True)(False)), true, 'Or(True)(False) is True');
        Test.assertEquals(unchurch(Or(False)(False)), false, 'Or(False)(False) is False');
    });
    it('Xor', () => {
        Test.assertEquals(unchurch(Xor(True)(True)), false, 'Xor(True)(True) is False');
        Test.assertEquals(unchurch(Xor(True)(False)), true, 'Xor(True)(False) is True');
    });
});


const True = T => F => T;
const False = T => F => F;

const unchurch = Boolean => {
    if (typeof Boolean !== 'function') {
        throw new Error(`Church boolean should be a function returning a function, instead got "${Boolean}"`);
    }
    const temp = Boolean(true);
    if (typeof temp !== 'function') {
        throw new Error(`Church boolean should be a function returning a function, instead got "${Boolean}"`);
    }
    return temp(false);
};
