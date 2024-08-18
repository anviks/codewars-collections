# [Born to be chained](https://www.codewars.com/kata/54c27ef1fb7da0118600046a)

Function composition is a powerful technique. For example:



But in complex expressions, composition may be difficult to understand. For example:



In this kata, we will implement a function that allows us to perform this by applying a fluid style:


Your job is implement the `chain` function:


As you can see, this function receives the methods to be chained and returns an object that allows you to call the chained methods. The result is obtained by calling the `execute` method.

Chained functions receive an arbitrary number of arguments. The first function in the chain receives all its arguments. In the other functions, the first argument is the result of the previous function and then it only receives the remainder arguments (second, third, etc.). The tests always pass the appropriate arguments and you do not have to worry about checking this.


Note that the chain can be reused (the internal state is not stored):



Other examples:



