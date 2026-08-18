def count_frequencies(items):
    counts = {}
    for i in items:
        if i in counts: 
            counts[i] += 1
        else: 
            counts[i] = 1 
    return counts
        

print(count_frequencies([1, 1, 2, 3, 3, 3]))
print(count_frequencies(["drama", "acción", "drama", "comedia"]))
print(count_frequencies([]))

