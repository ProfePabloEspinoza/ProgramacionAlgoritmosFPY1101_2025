import random

num1 = int(input("Ingrese el primer número (menor): "))
num2 = int(input("Ingrese el segundo número (mayor): "))

if num1 < num2:
    
    punto_medio = (num1 + num2) / 2
    
    rango = num2 - num1
    ajuste = rango * 0.2
    
    if random.randint(0, 1) == 0:
        numero_secreto = punto_medio + ajuste
    else:
        numero_secreto = punto_medio - ajuste
    numero_secreto = int(numero_secreto)
    
    intentos = 3
    intento1 = 0
    intento2 = 0
    
    adivinanza = int(input("Intento 1 - Adivina el número: "))
    if adivinanza == numero_secreto:
        print("Felicitaciones, pudiste adivinar")
    else:
        if adivinanza < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
        intento1 = adivinanza
        intentos = intentos - 1
        
        if intentos > 0:
            adivinanza = int(input("Intento 2 - Adivina el número: "))
            if adivinanza == numero_secreto:
                print("Felicitaciones, pudiste adivinar")
            else:
                if adivinanza < numero_secreto:
                    print("El número es mayor")
                else:
                    print("El número es menor")
                
                distancia1 = numero_secreto - intento1
                if distancia1 < 0:
                    distancia1 = -distancia1
                distancia2 = numero_secreto - adivinanza
                if distancia2 < 0:
                    distancia2 = -distancia2
                
                if distancia1 < distancia2:
                    print(f"Pista: Tu primer intento ({intento1}) estuvo más cerca")
                else:
                    print(f"Pista: Tu segundo intento ({adivinanza}) estuvo más cerca")
                
                intento2 = adivinanza
                intentos = intentos - 1
                
                if intentos > 0:
                    adivinanza = int(input("Intento 3 - Adivina el número: "))
                    if adivinanza == numero_secreto:
                        print("Felicitaciones, pudiste adivinar")
                    else:
                        print("Perdiste")
                        print(f"El número correcto era: {numero_secreto}")
else:
    print("Error: El primer número debe ser menor que el segundo.")