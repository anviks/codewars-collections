/*
 * https://www.codewars.com/kata/583203e6eb35d7980400002a
 */

export function countSmileys(arr) {
    let pattern = /[:;][-~]?[)D]/;
    let count = 0;
    for (const emoji of arr) {
        count += pattern.test(emoji);
    }
    return count;
}
