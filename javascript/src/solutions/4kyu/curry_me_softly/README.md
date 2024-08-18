# [Curry me softly](https://www.codewars.com/kata/55ba24f1cb367c48ac0000a2)

## Caveat

Currying is not exactly what is described below. Stretch your mind!

## Task

Create a function which accepts a single argument of another function and returns a "curried" version of that function.

Currying is a technique named (as is the language Haskell) after the mathematician Haskell Curry which allows a function's arguments to be fed to it through separate instances of running that function. For example, take the following function:

This function would normally be invoked like so:

A "curried" version of this function could be executed in either of the following ways

Or:

Your goal in this Kata is to produce a higher-order function that accepts another function as an argument and returns a "curried" version of that function.

This "curried" version of the original function should expand its arguments when invoked with arguments. It should allow multiple arguments to be passed into each invocation.

It should execute the original function and then restore that function's original argument-less state when invoked without arguments.

See example here, assuming `curryAdder` from above has been created already:

For fun, let's make sure this works with native global functions and methods too! (will involve some context)

Context is to be fixed the first time the "curried" function is called after creation.

Happy coding! :)