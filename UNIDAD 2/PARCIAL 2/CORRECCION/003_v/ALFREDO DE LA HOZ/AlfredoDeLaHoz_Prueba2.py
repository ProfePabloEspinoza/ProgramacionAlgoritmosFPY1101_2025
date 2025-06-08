#Prueba2: Alfredo De La Hoz
num1 = int(input("Ingresa un numero entero: "))
num2 = int(input("Ingresa un segundo numero entero (mayor que el primero): "))
if num1 >= num2:
    print("El primer numero debe ser menor que el segundo.")
else:
    puntomedio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2
    numerorandom = puntomedio + (ajuste if (num1 * num2) % 2 == 0 else -ajuste)
#se generan los intentos
intento_1 = int(input("Intento 1, adivina el numero: "))
if intento_1 == round(numerorandom):
        print("Adivinaste!")
else:
    if intento_1 < numerorandom:
     print("El numero es mayor")
    else:
     print("El numero es menor")
#segundo intento
    intento_2 = int(input("Intento 2, trata de adivinar el numero: "))
    if intento_2 == round(numerorandom):
            print("adivinaste!!!")
    else:
     if intento_2 < numerorandom:
                print("El numero es mayor")
     else:
                print("El numero es menor")
# Tercer intento
    intento_3 = int(input("ultimo intento! adivina el numero: "))
    if intento_3 == round(numerorandom):
                print("Felicitaciones, pudiste adivinar!")
    else:
                print("Perdiste. el numero secreto era:", round(numerorandom))