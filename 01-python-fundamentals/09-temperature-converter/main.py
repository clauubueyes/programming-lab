
def celsius_to_fahrenheit(temperature):
    celsius = temperature
    farenheit = (celsius * (9/5)) + 32
    return round(farenheit, 2)

def fahrenheit_to_celsius(temperature):
    fahrenheit=temperature
    celsius = ((fahrenheit - 32) * (5/9))
    return round(celsius, 2)

while True: 
    print("\n--- CONVERTIDOR DE TEMPERATURA ---")
    print("1: Celsius a Fahrenheit")
    print("2: Fahrenheit a Celsius")
    print("3: Salir")

    try: 
        option = int(input("Escoja una opción (1, 2 o 3):"))
        if option == 3: 
            print("Hasta Luego")
        if option in (1,2) :
            temperature = float(input("Introduce la temperatura: "))

            if option == 1:  
                print(f"{temperature}°C = {celsius_to_fahrenheit(temperature)}°F")
            elif option == 2: 
                print(f"{temperature}°F = {fahrenheit_to_celsius(temperature)}°C")
            break
        else: 
            print("Introduce una opción válida")
    except ValueError:
        print("Error: Debes introducir un número válido.")

