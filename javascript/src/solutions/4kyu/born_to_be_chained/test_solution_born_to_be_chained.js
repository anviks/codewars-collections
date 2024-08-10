/*
 * https://www.codewars.com/kata/54c27ef1fb7da0118600046a
 */

import { chain } from './solution_born_to_be_chained.js';
import { assert } from 'chai';
const { strictEqual } = assert;

describe("sample tests", function () {
	function sum(x, y) {
		return x + y;
	}

	const c = chain({sum});

	const c1 = c.sum(3, 4);
	const c2 = c.sum(1, 2);

	it('should return the correct value', function () {
		strictEqual(c1.execute(), 7);
		strictEqual(c2.execute(), 3);
	});

	const c11 = c1.sum(5);
	const c12 = c1.sum(20);

	it('should be reusable for new calls', function () {
		strictEqual(c11.execute(), 12);
		strictEqual(c12.execute(), 27);
	});
});

describe("custom tests", function () {
	function sum(x, y) {
		return x + y;
	}

	function double(x) {
		return sum(x, x);
	}

	function minus (x, y) {
		return x - y;
	}

	function addOne(x) {
		return sum(x, 1);
	}

	const c = chain({sum, minus, double, addOne});
	
	const c1 = c.sum(1, 2);
	const c2 = c1.double();
	const c3 = c1.addOne();
	
	it('should return the correct value', function () {
		strictEqual(c1.execute(), 3);
		strictEqual(c2.execute(), 6);
		strictEqual(c3.execute(), 4);
	});
	
	const c4 = c1.sum(5);
	const c5 = c4.addOne();
	const c6 = c4.sum(3);
	
	it('should return the correct value', function () {
		strictEqual(c5.execute(), 9);
		strictEqual(c6.execute(), 11);
	});
	
	it('should return the correct value', function () {
		strictEqual(c4.execute(), 8);
	});
	
	it('should return the correct value', function () {
		strictEqual(c1.execute(), 3);
	});
});
