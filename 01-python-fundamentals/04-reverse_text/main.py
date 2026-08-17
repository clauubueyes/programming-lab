def reverse_text(text): 
    reverse = ""
    for character in text: 
        reverse = character + reverse
            
    return reverse

text = input("escribe un texto: ")
print(reverse_text(text))