This is the second part of this kata series. First part is [here](https://www.codewars.com/kata/simple-assembler-interpreter/).

We want to create an interpreter of assembler which will support the following instructions:

- <br> 

## Input format:

The function/method will take as input a multiline string of instructions, delimited with EOL characters. Please, note that the instructions may also have indentation for readability purposes.

For example:

```python
program = """
; My first program
mov  a, 5
inc  a
call function
msg  '(5+1)/2 = ', a    ; output message
end

function:
	div  a, 2
	ret
"""
assembler_interpreter(program)
```
The above code would set register ```a``` to 5, increase its value by 1, calls the subroutine function, divide its value by 2, returns to the first call instruction, prepares the output of the program and then returns it with the ```end``` instruction. In this case, the output would be ```(5+1)/2 = 3```.

