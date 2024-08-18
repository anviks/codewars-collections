/*
 * https://www.codewars.com/kata/53c8b29750fe70e4a2000610
 */

import { ArrayComprehension } from './solution_haskell_list_dot_notation.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    expect: assert.isTrue,
    expectError: (message, fn) => assert.throws(fn, null, null, message)
};

describe('ArrayComprehension tests', function() {

    it('Empty list test', function() {
        var list = ArrayComprehension({ generator: '' });
        Test.assertSimilar(list, []);
        Test.assertSimilar(ArrayComprehension({}), []);
        Test.assertSimilar(ArrayComprehension({ generator: '    ' }), []);
    });

    it('One element test', function() {
        var list = ArrayComprehension({ generator: '1' });
        Test.assertSimilar(list, [1]);
    });

    it('Two elements test', function() {
        Test.assertSimilar(ArrayComprehension({ generator: '1,4' }), [1, 4]);
        Test.assertSimilar(ArrayComprehension({ generator: ' 1   ,  4  ' }), [1, 4]);
    });

    it('Multiple elements test', function() {
        Test.assertSimilar(ArrayComprehension({ generator: '1,4,6,3,-2' }), [1, 4, 6, 3, -2]);
    });

    it('Range tests', function() {
        Test.assertSimilar(ArrayComprehension({ generator: '1,3..4' }), [1, 3]);
        Test.assertSimilar(ArrayComprehension({ generator: '1,2..2' }), [1, 2]);
        Test.assertSimilar(ArrayComprehension({ generator: '3,2..2' }), [3, 2]);
        Test.assertSimilar(ArrayComprehension({ generator: '5..3' }), []);
        Test.assertSimilar(ArrayComprehension({ generator: '90..80' }), []);
        Test.assertSimilar(ArrayComprehension({ generator: '1,90..80' }), [1]);
        Test.assertSimilar(ArrayComprehension({ generator: '1..5' }), [1, 2, 3, 4, 5]);
        Test.assertSimilar(ArrayComprehension({ generator: '1,4..12' }), [1, 4, 7, 10]);
        Test.assertSimilar(ArrayComprehension({ generator: '12,10..4' }), [12, 10, 8, 6, 4]);
    });
});
