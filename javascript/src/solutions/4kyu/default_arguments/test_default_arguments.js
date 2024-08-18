/*
 * https://www.codewars.com/kata/52605419be184942d400003d
 */

import { defaultArguments } from './solution_default_arguments.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    assertNaN: assert.isNaN,
};

describe('Tests', () => {
    it('Sample tests', () => {
        function add(a, b) {
            return a + b;
        }

        let add_ = defaultArguments(add, { b: 9 });
        Test.assertEquals(add_(10), 19);
        Test.assertEquals(add_(10, 5), 15);
        Test.assertNaN(add_());
        
        add_ = defaultArguments(add_, { b: 3 });
        Test.assertEquals(add_(10), 13);
        
        add_ = defaultArguments(add_, { b: 3, a: 2 });
        Test.assertEquals(add_(10), 13);
        Test.assertEquals(add_(), 5);
        
        add_ = defaultArguments(add_, { c: 3 });
        Test.assertNaN(add_(10));
        Test.assertEquals(add_(10, 10), 20);
    });
    
    it('Without parameters', () => {
        const five = function() {
            return 5;
        };

        let wtf = defaultArguments(five, { g: 4 });
        Test.assertEquals(wtf(), 5);
    });
});
