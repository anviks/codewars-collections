/*
 * https://www.codewars.com/kata/55ba24f1cb367c48ac0000a2
 */

import { CurryIt } from './solution_curry_me_softly.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    expect: assert.isTrue,
};

describe('Tests', () => {
    it('test', () => {
        function adder() {
            return [].slice.call(arguments).reduce(function(a, b) {
                return a + b;
            }, 0);
        }

        var curryAdder = CurryIt(adder);

        curryAdder(1);
        curryAdder(99);
        Test.expect(curryAdder() === 100, 'Basic, single-argument function feeding currying is not working');

        curryAdder(1);
        curryAdder(5);
        Test.expect(curryAdder() === 6, 'wiping the function is not working');

        curryAdder(1, 5, 1, 1, 1, 1, 1, 7);
        curryAdder(51, 4);
        curryAdder(9);
        Test.expect(curryAdder() === 82, 'accepting multiple arguments in one invocation (and adding them to the arguments of the curried function) is not working');

        var curryEval = CurryIt(eval);
        curryEval('var y = function(){return true}');
        curryEval();
        Test.expect(y(), 'accepting a native global function is not working');

        var curryReduce = CurryIt(Array.prototype.reduce);

        var exampleArray = [2, 3, 4];
        curryReduce.call(exampleArray, function(a, b) {
            return a + b;
        });
        curryReduce(8);
        Test.expect(curryReduce() === 17, 'accepting a native Array method is not working');
    });
});

