
promedio = float(input("Bienvenido, ingrese su promedio final del liceo: "))
decil = int(input("Indique cual es su decil (1/10): "))

arancel = 2200000
matricula = 95000

descuento = 0
descuento_matricula = 0

if promedio > 6.5 and (decil == 1 or decil == 2) :
    descuento = 0.25

elif promedio > 6.5 and (decil == 3 or decil == 4) :
    descuento = 0.18

elif 5.5 < promedio <= 6.5 and (decil == 1 or decil == 2) :
    descuento = 0.15

elif 5.5 < promedio <= 6.5 and (decil == 3 or decil == 4) :
    descuento = 0.12

if decil in [1 ,2, 3]:
    descuento_matricula = 0.12

    if promedio >= 6.0:

        descuento_matricula += 0.05


arancel_final = round(arancel * ( 1 - descuento))
matricula_final = round(matricula * ( 1 - descuento_matricula))


print(f"El valor del arancel es de: {arancel_final} CLP ")
print(f"El valor de la matricula es de: {matricula_final} CLP ")


# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// #


import random

num1 = int(input("Ingrese un numero minimo: "))
num2 = int(input("Ingrese un numero maximo: "))

if num1 < num2:
    punto_medio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2
    numero_random = round(random.uniform(punto_medio - ajuste, punto_medio + ajuste))

    primer_intento = 0

    for intento_num in range(1, 4):
        intento = int(input(f"Intento {intento_num}: Adivina el numero: "))

        if intento == numero_random:
            print("Felicidades, adivinaste el numero!")
            break
        
        elif intento < numero_random:
            print("El numero es mayor.")
        else:
            print("El numero es menor.")

        if intento_num == 1:
            primer_intento = intento  

        if intento_num == 2:
            distancia_num1 = abs(primer_intento - numero_random)
            distancia_num2 = abs(intento - numero_random)

            if distancia_num1 < distancia_num2:
                print(f"Le dare una pista, el numero esta mas cerca del {primer_intento}")
            elif distancia_num2 < distancia_num1:
                print(f"Le dare una pista, el numero esta mas cerca del {intento}")
            else:
                print("Te dare una pista, ambos intentos estan igual de lejos.")

    else:
        print("Perdiste.")
        print(f"El numero correcto era: {numero_random}")
else:
    print("El primer numero debe ser menor que el segundo")










