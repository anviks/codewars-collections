/*
 * https://www.codewars.com/kata/54c27ef1fb7da0118600046a
 */


class Chain {
    constructor(functions) {
        this.value = null;

        for (const func in functions) {
            this[func] = (...args) => {
                if (this.value !== null) {
                    args.splice(0, 0, this.value);
                }
                const clone = new Chain(functions);
                clone.value = functions[func](...args);
                return clone;
            };
        }
    }

    execute() {
        return this.value;
    }
}

export function chain(functions) {
    return new Chain(functions);
}
