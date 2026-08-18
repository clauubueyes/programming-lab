def remove_duplicates(items): 
    clean_items = []
    
    for item in items:
        if item not in clean_items: 
            clean_items.append(item)
    return clean_items
     

print(remove_duplicates([1, 3, 3, 5, 7, 7, 9]))
print(remove_duplicates(["peli1", "peli2", "peli1", "peli3"]))
print(remove_duplicates([]))