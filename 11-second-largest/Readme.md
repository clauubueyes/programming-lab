## Second Largest Number

## Description 
Create a function find_second_largest(numbers) that receives a list of numbers and returns the second largest number in that list 

## Rules 
1. No sorting traps: Don't use .sort() or sorted() at first. We want to train the logic of traversing the list and comparing values ​​manually or iteratively.

2. Duplicates: If the list is [10, 10, 8, 5], the absolute maximum is 10. The second largest distinct number is 8.

3. Edge cases: If the list has less than 2 unique elements (example: [5] or [7, 7]), the function should return None. 

### Test: 
```
find_second_largest([3, 1, 4, 1, 5, 9, 2]) -> 5
find_second_largest([10, 10, 9]) -> 9
find_second_largest([5]) -> None
find_second_largest([7, 7, 7]) -> None

```