/*
 * https://www.codewars.com/kata/5a353a478f27f244a1000076
 */

import { sayJoke } from './solution_jokes_you_ve_been_awaiting_for_promise.js';
import { assert } from 'chai';


describe('Bad Christmas jokes', () => {
    const url = 'http://great.jokes/christmas';

    // Just a starting point to test async functions
    it('say the setup line', async () => {
        const joke = await sayJoke(url, 101);
        assert.strictEqual(joke.saySetup(), 'Who is Santa\'s favorite singer?');
    });
});

// Setup:
const jokeList = [
    {
        id: 101,
        setup: 'Who is Santa\'s favorite singer?',
        punchLine: 'Elf-is Presley!'
    },
    {
        id: 132,
        setup: 'What do Santa\'s little helpers learn at school?',
        punchLine: 'The elf-abet!'
    },
    {
        id: 144,
        setup: 'Where do elves go to dance?',
        punchLine: 'Christmas Balls!'
    },
    {
        id: 324,
        setup: 'Which of Santa’s reindeers have to mind their manners most?',
        punchLine: 'Rude-olph!'
    },
    {
        id: 628,
        setup: 'Why did the turkey join the band?',
        punchLine: 'Because it had the drumsticks!'
    },
    {
        id: 509,
        setup: 'How do snowmen get around?',
        punchLine: 'They ride an icicle'
    },
    {
        id: 207,
        setup: 'What do you call a bankrupt Santa?',
        punchLine: 'Saint Nickel-less!'
    }
];

const jokeJson = {
    jokes: jokeList
};

const jokesUrl = 'http://great.jokes/christmas';

export function fetch(url) {
    if (jokesUrl === url) {
        return Promise.resolve(jsonResolve(jokeJson));
    }

    return Promise.resolve(jsonResolve({
        differentApi: [{
            jokeId: 0,
            bad: 'data'
        }]
    }));
}

function jsonResolve(shape) {
    return {
        json: () => Promise.resolve(shape)
    };
}

