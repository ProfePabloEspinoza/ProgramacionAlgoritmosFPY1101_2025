
import random

print("RANGO NUMERICO")
#El primer numero debe ser menor que el segundo.

print("Ingrese un primer numero")
num1 = float (input(""))

print("Ingrese un segundo numero")
num2 = float (input(""))

#calcular punto medio de los numeros
punto_medio = num1 + num2 / 2

#determinar el 20%
ajuste = (num2-num1) * 0.2


decision = random.randint(1,2)

if decision == 1:
    numero_aleatorio = punto_medio + ajuste
    

if decision == 2:
    numero_aleatorio = punto_medio - ajuste
   

#juego de adivinar el numero
intentos = 3

while intentos>0:

    print("Desafio de adivinar el numero")
    print("Cuentas con ",intentos, " restantes")
    
    adivinar= int (input(""))

    if intentos == 1:
        if adivinar != numero_aleatorio: 
            if adivinar > numero_aleatorio:
             print("El numero a adivinar es menor al ingresado")
             intentos= intentos-1

            if adivinar < numero_aleatorio:
                print("El numero a adivinar es mayor al ingresado")
                intentos= intentos-1

    if intentos >3:
        if adivinar != numero_aleatorio: 
            if adivinar > numero_aleatorio:
                print ("Perdistes, el numero era ",numero_aleatorio)
                intentos= intentos-1

            if adivinar < numero_aleatorio:
                intentos= intentos-1
                print("Perdistes, el numero era ",numero_aleatorio)

    if adivinar == numero_aleatorio: 
        print("Felicitaciones, pudiste adivinar el numero")
        









