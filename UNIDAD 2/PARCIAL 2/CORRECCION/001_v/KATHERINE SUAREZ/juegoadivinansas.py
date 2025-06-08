import random

num1 = int(input("Límite inferior: "))
num2 = int(input("Límite superior: "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo.")
else:
    numero = round((num1 + num2) / 2 + random.uniform(-(num2 - num1) * 0.2, (num2 - num1) * 0.2))
    intentos = []

    for i in range(3):
        intento = int(input(f"Intento {i+1}: "))
        intentos.append(intento)

        if intento == numero:
            print("¡Adivinaste!")
            break
        elif i < 2:
            print("nro Mayor" if intento < numero else "nro Menor")
            if i == 1:
                print(f"Pista: Más cerca de {min(intentos, key=lambda x: abs(x - numero))}.")
    else:
        print(f"Perdiste. Era {numero}.")