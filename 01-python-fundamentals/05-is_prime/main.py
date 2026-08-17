
def is_prime(number): 
    if number > 1:
        for i in range(2, number):  
            if number % i == 0: 
                return False
        return True
    return False

while True: 
    try: 
        number = int(input("Introduce un número: "))
        print(is_prime(number))
        break
    except ValueError: 
        print("Solo puedes introducir números enteros")