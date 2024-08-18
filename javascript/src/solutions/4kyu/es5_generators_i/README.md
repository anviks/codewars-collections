# [ES5 Generators(i)](https://www.codewars.com/kata/53c29a6abb5187180d000b65)

This is the first part of three ([part2](http://www.codewars.com/kata/es5-generators-ii), [part3](http://www.codewars.com/kata/es5-generators-iii)).

Generators and Iterators are ES6 features that allow things like this:



Using them in this way, we can do amazing things:



The goal of this kata is to implement pseudo-generators with ES5.

The first thing to do is to implement the generator function:



`generator(sequencer[, arg1, arg2, ...])` receives a *sequencer* function to generate the sequence and returns an object with a `next()` method. When the `next()` method is invoked, the next value is generated. The method could receive as well optional arguments to be passed to the *sequencer* function.

This is an example of a dummy sequencer:



To test `generator()`, you could use `dummySeq()` in this way:



When you're done, you should implement the following generators (I think the functions are self explanatory):



You can use any of them in the same way:



There are some sequences which are infinite and others are not. For example:

* primeSeq: Is infinite
* partialSumSeq: Is limited to the passed values.

When the sequence is done (in finite sequences), if you call `seq.next()` again, it should produce an error.

Good luck!