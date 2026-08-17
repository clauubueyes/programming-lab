def is_anagram(word1, word2):
    clean1 = word1.lower().replace(" ", "")
    clean2 = word2.lower().replace(" ", "")
    return sorted(clean1) == sorted(clean2)

word1 = input("Introduce la primera palabra: ")
word2 =  input("Introduce la segunda palabra: ")
print(is_anagram(word1, word2))