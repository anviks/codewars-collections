/*
 * https://www.codewars.com/kata/554ca54ffa7d91b236000023
 */

import { deleteNth } from './solution_delete_occurrences_of_an_element_if_it_occurs_more_than_n_times.js';
import { assert } from 'chai';

describe('Tests', () => {
    it('test', () => {
        assert.sameOrderedMembers(deleteNth([20, 37, 20, 21], 1), [20, 37, 21]);
        assert.sameOrderedMembers(deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3), [1, 1, 3, 3, 7, 2, 2, 2]);
        assert.sameOrderedMembers(deleteNth([12, 39, 19, 39, 39, 19, 12], 1), [12, 39, 19]);
    });
});

