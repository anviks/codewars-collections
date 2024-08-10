/*
 * https://www.codewars.com/kata/59a421985eb5d4bb41000031
 */

await import('./solution_multi_line_task_hello_world.cjs');
import { assert } from 'chai';
import { dirname } from 'path';
import { fileURLToPath } from 'url';
import fs from 'node:fs';

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
    const solutionFile = fs.readFileSync(dirname(fileURLToPath(import.meta.url)) + '/solution_multi_line_task_hello_world.cjs', 'utf-8');
    const usercode = solutionFile.slice(solutionFile.indexOf('// @formatter:off') + '// @formatter:off\r\n'.length, solutionFile.indexOf('// @formatter:on'));
    
    it('Every line should have less than 2 characters', function() {
        const limit = 2;
        const lines = usercode.split('\r\n');
        Test.expect(Math.max(...lines.map(s => s.length)) < limit, 'Some lines of your code exceeded the character limit');
    });
    
    it('There should be less than 145 lines', function() {
        const limit = 145;
        const lines = usercode.split('\n');
        Test.expect(lines.length < limit, `Your code has ${lines.length} lines`);
    });
});
