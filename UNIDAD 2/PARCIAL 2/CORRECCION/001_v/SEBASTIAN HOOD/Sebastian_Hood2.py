import random

num_min = int(input("Ingrese el primer numero: (debe ser entero y menor que el segundo) "))
num_max = int(input("Ingrese el segundo numero: (debe ser entero y mayor que el primero) "))
# No entiendo la funcion del punto meddio y el ajuste en las instrucciones del ejercicio , asi que hice el programa seleccionando numeros al azar dentro del rango#
ajuste = (num_max - num_min) * 0.2
numero_aleatorio = random.randint(num_min, num_max)
intentos = 3
intentos_usuario = []

for intento in range(1, intentos + 1):
    guess = int(input(f"Intento {intento}: Adivina el número generado: "))
    intentos_usuario.append(guess)
    if guess == numero_aleatorio:
        print("¡Felicidades! Adivinaste el número.")
        break
    elif intento < intentos:
        if guess < numero_aleatorio:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        if intento == 2:
            distancia_1 = abs(intentos_usuario[0] - numero_aleatorio)
            distancia_2 = abs(intentos_usuario[1] - numero_aleatorio)
            if distancia_1 < distancia_2:
                print("Tu primer intento estuvo más cerca.")
            elif distancia_2 < distancia_1:
                print("Tu segundo intento estuvo más cerca.")
            else:
                print("Ambos intentos estuvieron igual de cerca.")
    else:
        print(f"Perdiste. El número correcto era: {numero_aleatorio}")