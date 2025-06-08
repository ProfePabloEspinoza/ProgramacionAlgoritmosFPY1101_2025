
#EJERCICIO 1



print("-----Calcule sus beneficios estudiantiles-----")

promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese su condición socioeconómica, decil 1 - 4: "))

arancel = 2200000
matricula = 95000

descuento = 0.0

if (promedio >= 6.5) and (decil == 1 or decil == 2):
    descuento = 0.25
elif (promedio >= 6.5) and (decil == 3 or decil == 4):
    descuento = 0.18
elif (5.5 <= promedio <= 6.5) and (decil == 1 or decil == 2):
    descuento = 0.15
elif (5.5 <= promedio <= 6.5) and (decil == 3 or decil == 4):
    descuento = 0.12
else:
    print("Alguno de los datos ha sido ingresado incorrectamente")

arancelfinal = int(arancel * (1 - descuento))

descuento_matricula = 0.0

if (promedio >= 6.0) and (decil == 1 or decil == 2 or decil == 3):
    descuento_matricula = 0.17 
elif (decil == 1 or decil == 2 or decil == 3):
    descuento_matricula = 0.12
else:
    matricula_final = matricula

matricula_final = int(matricula * (1 - descuento_matricula))

print(f"El valor del arancel es de: ${arancelfinal}")
print(f"El valor de la matricula es de: ${matricula_final}")

"""

#EJERCICIO 2

import random

print ("----Adivinar el número----- ")

num1 = int(input("Ingrese número límite inferior:"))
num2 = int(input("Ingrese número límite superior:"))

punto_medio = int((num1+num2)/2)
ajuste = int((num2-num1)*0.2)
num_aleatorio = int((random.randint(num1, num2)))
num_aleatorio_ajust = int(num_aleatorio - ajuste)

contador = 0
max_intentos = 3

while contador < max_intentos:
    adivina = int(input("Intente adivinar el numero generado, máximo 3 intentos: "))
    contador += 1

    if adivina == num_aleatorio_ajust:
        print ("Felicitaciones, pudiste adivinar")
        break

    if adivina != num_aleatorio_ajust:
        if contador == 1:
            if adivina > num_aleatorio_ajust:
                print ("Incorrecto, el número que ingresó es MAYOR al número generado")
            elif adivina < num_aleatorio_ajust:
                print ("Incorrecto, el número que ingresó es MENOR al número generado")
        if contador == 2:
            if adivina > num_aleatorio_ajust:
                print ("Incorrecto, el número que ingresó es MAYOR al número generado")
            elif adivina < num_aleatorio_ajust:
                print ("Incorrecto, el número que ingresó es MENOR al número generado")
        if contador == 3:
            print ("Perdiste")
            print (f"El número correcto es {num_aleatorio_ajust}")


"""