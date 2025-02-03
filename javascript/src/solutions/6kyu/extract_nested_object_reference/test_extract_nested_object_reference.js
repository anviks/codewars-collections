/*
 * https://www.codewars.com/kata/527a6e602a7db3456e000a2b
 */

import './solution_extract_nested_object_reference.js';
import { assert, config } from 'chai';

config.truncateThreshold = 0;

const obj = {
  person: {
    name: 'joe',
  },
};

describe('Tests', () => {
  it('test', () => {
    assert.strictEqual(obj.hash('person.name'), 'joe');
    assert.strictEqual(obj.hash('person.game.home'), undefined);
  });
});
