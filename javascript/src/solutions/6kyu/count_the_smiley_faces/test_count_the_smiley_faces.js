/*
 * https://www.codewars.com/kata/583203e6eb35d7980400002a
 */

import { countSmileys } from './solution_count_the_smiley_faces.js';
import { assert } from 'chai';

describe('Basic testing', function() {
    it('Example tests', () => {
        assert.strictEqual(countSmileys([]), 0);
        assert.strictEqual(countSmileys([':D', ':~)', ';~D', ':)']), 4);
        assert.strictEqual(countSmileys([':)', ':(', ':D', ':O', ':;']), 2);
        assert.strictEqual(countSmileys([';]', ':[', ';*', ':$', ';-D']), 1);
    });
});
