/*
 * https://www.codewars.com/kata/53c29a6abb5187180d000b65
 */

import { generator, rangeSeq, primeSeq, factorialSeq, partialSumSeq, dummySeq, fibonacciSeq } from './solution_es5_generators_i.js';
import { assert } from 'chai';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    expect: assert.isTrue,
    expectError: (message, fn) => assert.throws(fn, null, null, message),
};


describe('ES5 Dummy generator', function() {
    it('Test dummy generator', function() {
        var seq = generator(dummySeq);
        Test.assertEquals(seq.next(), 'dummy');
        Test.assertEquals(seq.next(), 'dummy');
        Test.assertEquals(seq.next(), 'dummy');
    });
});

describe('ES5 Simple Generators', function() {

    it('Test factorial generator', function() {
        var seq = generator(factorialSeq);
        Test.assertEquals(seq.next(), 1); // 0! = 1
        Test.assertEquals(seq.next(), 1); // 1! = 1
        Test.assertEquals(seq.next(), 2); // 2! = 2
        Test.assertEquals(seq.next(), 6); // 3! = 6
        Test.assertEquals(seq.next(), 24); // 4! = 6
    });

    it('Test Fibonacci generator', function() {
        var seq = generator(fibonacciSeq);
        Test.assertEquals(seq.next(), 1); // fib(0) = 1
        Test.assertEquals(seq.next(), 1); // fib(1) = 1
        Test.assertEquals(seq.next(), 2); // fib(2) = 2
        Test.assertEquals(seq.next(), 3); // fib(3) = 3
        Test.assertEquals(seq.next(), 5); // fib(4) = 5
        Test.assertEquals(seq.next(), 8); // fib(5) = 8
        Test.assertEquals(seq.next(), 13); // fib(6) = 13
    });

    it('Test Range generator', function() {
        var seq = generator(rangeSeq, 5, 3); // 5,8,11,14,17
        Test.assertEquals(seq.next(), 5);
        Test.assertEquals(seq.next(), 8);
        Test.assertEquals(seq.next(), 11);
        Test.assertEquals(seq.next(), 14);
    });

    it('Test Prime Numbers generator', function() {
        var seq = generator(primeSeq);
        Test.assertEquals(seq.next(), 2);
        Test.assertEquals(seq.next(), 3);
        Test.assertEquals(seq.next(), 5);
        Test.assertEquals(seq.next(), 7);
        Test.assertEquals(seq.next(), 11);
        Test.assertEquals(seq.next(), 13);
        Test.assertEquals(seq.next(), 17);
        Test.assertEquals(seq.next(), 19);
    });

    it('Test partial sum generator', function() {
        var seq = generator(partialSumSeq, -1, 4, 2, 5);
        Test.assertEquals(seq.next(), -1);
        Test.assertEquals(seq.next(), 3);
        Test.assertEquals(seq.next(), 5);
        Test.assertEquals(seq.next(), 10); //End of sequence
        Test.expectError('End of sequence error expected', seq.next);
    });
});
