def filter_movies_by_runtime(movies, runtime):
    res = []
    for movie in movies: 
        if (movie.get("runtime", 0) <= runtime): 
            title= movie.get("title")
            res.append(title)
    return res



movies = [
    {"title": "Shrek", "runtime": 90},
    {"title": "Titanic", "runtime": 194},
    {"title": "Cars", "runtime": 117},
    {"title": "Up", "runtime": 96}
]

print(filter_movies_by_runtime(movies, 120))