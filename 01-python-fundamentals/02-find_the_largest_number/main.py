"""
lista = [] 
cont = 1

while cont <= 3: 
    number = int(input(f"introduce un número {cont} : "))  
    cont = cont +1  
    lista.append(number) 

lista.sort()
print(f"El número mas grande es {lista[-1]}")
"""


numbers = []
cont = 1

def largest_number(numbers):
    res = numbers[0]
    for i in numbers:
        if i > res: 
            res = i
    return res

while cont <= 3: 
    try: 
        number = float(input(f"introduce un número {cont} : "))  
        cont = cont +1  
        numbers.append(number)
    except ValueError: 
        print("Solo puedes poner números") 

print(f"the largest number is: {largest_number(numbers)}")

print(largest_number([12, 7, 25]))
print(largest_number([100, 2, 50]))
print(largest_number([-5, -20, -1]))