""" 
def par_o_impar(): 
    while (True):
        try:  
            a = int(input("Introduce un número entero: "))
            if  a % 2 == 0: 
                print(f"El número {a} es par")
            else: 
               print(f"El número {a} es impar")
            break
        except ValueError: 
            print("Solo puedes introducir números enteros")
   
    return None

par_o_impar()
""" 
def es_par(a):
    return a % 2 == 0

while(True): 
    try:
        a = int(input("Introduce un número entero: "))
        if es_par(a): 
           print(f"El número {a} es par")
        else: 
           print(f"El número {a} es impar")
        break
    except ValueError: 
        print("Solo puedes introducir números enteros")