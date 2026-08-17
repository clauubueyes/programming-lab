# Find the Largest Number

## Description

Create a program that receives three numbers and determines which one is the largest.

### Rule

The built-in `max()` function cannot be used.

## Example

### Input

```text
Introduce a number 1: 23
Introduce a number 2: 45
Introduce a number 3: 1213
```
### Output: 
```The largest number is: 1213``` 

## What I lean: 

1. How to create and work with lists.
2. How to add elements to a list using append().
3. How to iterate over a list using a for loop.
4. How to keep track of the largest value found while iterating through a list.
5. How return works and how it ends the execution of a function.
6. How to handle invalid user input using try/except.
7. How indentation affects the structure of Python code.
8. The importance of choosing descriptive variable names.

## Algorithm
To find the largest number without using max():

1. Use the first number as the initial largest value.
2. Iterate through the list.
3. Compare each number with the current largest value.
4. If the current number is larger, update the largest value.
5. Return the largest value after checking all numbers.