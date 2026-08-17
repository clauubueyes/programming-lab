
def is_palindrome(text): 
    reverse = ""
    clean_text = text.lower().replace(" ", "")
    for character in clean_text:
        reverse = character + reverse 
    return reverse==clean_text


text = input("Introduce un texto: ")
print(is_palindrome(text))