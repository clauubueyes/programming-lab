def count_word(text): 
    clean_text = text.lower().split()
    return len(clean_text) 

text = input("Introduce un texto: ")
print(count_word(text))