## Movie Runtime Filter

### Description 
Create a function called filter_movies_by_runtime that receives a list of movies and a maximum number of minutes.

The function should return a new list containing only the titles of movies whose duration is less than or equal to the indicated limit.

## Rules 
1. You must create a function called filter_movies_by_runtime.
2. You must use a for to cycle through the movies.
3. You must use an if condition to check the duration.
4. You must create a new list to store the results.
5. You can use .append().
6. You cannot modify the original list.
7. You cannot use external filter functions like filter().
## Example 
movies = [
    {"title": "Shrek", "runtime": 90},
    {"title": "Titanic", "runtime": 194},
    {"title": "Cars", "runtime": 117},
    {"title": "Up", "runtime": 96}
]

filter_movies_by_runtime(movies, 120)

