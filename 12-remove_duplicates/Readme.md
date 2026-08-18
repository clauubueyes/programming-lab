## REMOVE DUPLICATES 

### Description 
Create a function remove_duplicates(items) that receives a list with repeated elements and returns a new list preserving only the first order of appearance of each element. 

### Rules 
1. Don't use the quick list(set(items)) conversion, as Python sets are not guaranteed to maintain the original order of the elements.
2. The function must return a new list without modifying the original list. 

### Test

```
remove_duplicates([1, 3, 3, 5, 7, 7, 9]) -> [1, 3, 5, 7, 9]
remove_duplicates(["peli1", "peli2", "peli1", "peli3"]) -> ["peli1", "peli2", "peli3"]
remove_duplicates([]) -> []
```