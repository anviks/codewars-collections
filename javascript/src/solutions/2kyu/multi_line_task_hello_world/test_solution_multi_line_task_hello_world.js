/*
 * https://www.codewars.com/kata/5935558a32fb828aad001213
 */

import { f } from './solution_multi_line_task_hello_world.js';
import { assert } from 'chai';
import fs from 'node:fs';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const Test = {
    assertSimilar: assert.deepEqual,
    assertEquals: assert.strictEqual,
    assertDeepEquals: assert.deepEqual,
    expect: assert.isTrue
};

describe('Basic tests', function() {
    it('It should work for basic tests', function() {
        Test.assertEquals(f(), 'Hello, world!');
    });
});

describe('Code length check', function() {
    const solutionFile = fs.readFileSync(dirname(fileURLToPath(import.meta.url)) + '/solution_multi_line_task_hello_world.js', 'utf-8');
    const usercode = solutionFile.slice(solutionFile.indexOf('// @formatter:off') + '// @formatter:off\r\n'.length, solutionFile.indexOf('// @formatter:on'));
    
    it('Every line should have less than 3 characters', function() {
        const limit = 3;
        const lines = usercode.split('\r\n');
        Test.expect(Math.max(...lines.map(s => s.length)) < limit, `Some lines of your code exceeded the character limit`);
    });
    
    it('There should be less than 40 lines', function() {
        const limit = 40;
        const lines = usercode.split('\n');
        Test.expect(lines.length < limit, `Your code has ${lines.length} lines`);
    });
});
