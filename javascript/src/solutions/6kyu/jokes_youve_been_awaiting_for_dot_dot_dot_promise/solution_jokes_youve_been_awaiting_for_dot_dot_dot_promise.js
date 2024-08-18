/*
 * https://www.codewars.com/kata/5a353a478f27f244a1000076
 */

import { fetch } from './test_jokes_youve_been_awaiting_for_dot_dot_dot_promise.js';

class Joke {
    constructor(setup, punchLine) {
        this.setup = setup;
        this.punchLine = punchLine;
    }

    saySetup() {
        return this.setup;
    }

    sayPunchLine() {
        return this.punchLine;
    }
}

export function sayJoke(apiUrl, jokeId) {
    return fetch(apiUrl).then(r => {
        return r.json();
    }).then(jokes => {
        if (jokes.jokes === undefined) {
            throw new Error(`No jokes at url: ${apiUrl}`);
        }
        const joke = jokes.jokes.find(j => j.id === jokeId);
        if (joke) {
            return new Joke(joke.setup, joke.punchLine);
        } else {
            throw new Error(`No jokes found id: ${jokeId}`);
        }
    });
}