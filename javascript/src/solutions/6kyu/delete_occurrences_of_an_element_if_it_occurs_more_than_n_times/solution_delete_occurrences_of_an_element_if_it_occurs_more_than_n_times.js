/*
 * https://www.codewars.com/kata/554ca54ffa7d91b236000023
 */

export function deleteNth(arr, n) {
    let counts = {};
    let newArr = [];

    for (const element of arr) {
        if (counts[element] === n) continue;
        counts[element] = (counts[element] || 0) + 1;
        newArr.push(element);
    }

    return newArr;
}

