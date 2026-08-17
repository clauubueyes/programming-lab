
def count_vowels(text): 
    cont = 0
    for characters in text.lower(): 
        if characters in "aeiou": 
            cont += 1
    return cont

while True: 
    text = str(input("Escribe un texto: "))
    print(f"El texto tiene {count_vowels(text)} vocales ")
    break
    



