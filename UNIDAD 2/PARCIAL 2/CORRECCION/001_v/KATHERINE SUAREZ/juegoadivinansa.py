import random
print("Bienvenido al juego de adivinanza de números.")
print("Elige dos números, el primero debe ser menor que el segundo.")           

num1 = int(input("Ingresa el primer número (menor): "))
num2 = int(input("Ingresa el segundo número (mayor): "))

if num1 >= num2:
    print("El primer número debe ser menor que el segundo.")
else:
    punto_medio = (num1 + num2) / 2 # Calcula el punto medio
    ajuste = (num2 - num1) * 0.2 # Ajuste del rango
    numero_secreto = round(punto_medio + random.uniform(-ajuste, ajuste))

    print("¡Intenta adivinar el número! Tienes 3 intentos.")

    intentos = []
    for i in range(3):
        intento = int(input(f"Intento {i+1}: "))
        intentos.append(intento)

        if intento == numero_secreto:
            print("¡Felicitaciones, pudiste adivinar!")
            break
        elif i < 2:
            print("El número es mayor" if intento < numero_secreto else "El número es menor")

            if i == 1:
                print(f"Pista: El número {min(intentos, key=lambda x: abs(x - numero_secreto))} estuvo más cerca.")
    else:
        print(f"Perdiste. El número correcto era {numero_secreto}")