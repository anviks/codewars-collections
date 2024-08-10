/*
 * https://www.codewars.com/kata/53c29a6abb5187180d000b65
 */

export function generator(sequencer) {
    return { next: sequencer.apply(null, [].slice.call(arguments, 1)) };
}

export function dummySeq() {
    return function() {
        return 'dummy';
    };
}

export function factorialSeq() {
    let pos = 0, count = 1;
    return function() {
        if (pos === 0) {
            pos++;
            return count;
        }
        return count *= pos++;
    };
}

export function fibonacciSeq() {
    let last = 0, now = 1, next = 1;
    return function() {
        last = now;
        now = next;
        next = last + now;
        return last;
    };
}

export function rangeSeq(start, step) {
    return function() {
        const tmp = start;
        start += step;
        return tmp;
    };
}


//Uses an ever-expanding Sieve of Eratosthenes to test for primes
const sieve = [2, 3, 5, 7, 11];

export function primeSeq() {
    let count = 0;
    return function() {
        if (sieve[count] == null) generateNextPrime();
        return sieve[count++];
    };
}

export function partialSumSeq() {
    let seq = [].slice.call(arguments), pos = 0, running = seq[pos];
    return function() {
        const tmp = running;
        if (isNaN(tmp)) throw Error('End of sequence error');
        running += seq[++pos];
        return tmp;
    };
}

function generateNextPrime() {
    let current = sieve[sieve.length - 1] + 2;
    while (true) {
        if (isPrimeFromSieve(current)) {
            sieve.push(current);
            break;
        }
        current += 2;
    }
}

function isPrimeFromSieve(num) {
    const max = Math.ceil(Math.sqrt(num));
    for (let i = 0; i < sieve.length; i++) {
        if (num % sieve[i] === 0) return false;
        else if (max < sieve[i]) return true;
    }
    return true;
}