/*
 * https://www.codewars.com/kata/5324945e2ece5e1f32000370
 */

export function sumStrings(a, b) {
    let smaller = Math.min(a.length, b.length) === a.length ? a : b;
    let larger = smaller === a ? b : a;
    let lengthDifference = larger.length - smaller.length;
    let carry = 0;
    let result = '';

    for (let i = smaller.length - 1; i >= 0; i--) {
        let tempResult = +smaller.at(i) + +larger.at(i + lengthDifference) + carry;
        carry = 0;

        if (tempResult > 9) {
            carry = 1;
            tempResult %= 10;
        }

        result = tempResult + result;
    }

    if (lengthDifference) {
        result = larger.slice(0, lengthDifference - 1)
            + (+larger.at(lengthDifference - 1) + carry)
            + result;
        carry = 0;
    }

    if (carry) result = '1' + result;

    return result.replace(/^0+/, '');
}
