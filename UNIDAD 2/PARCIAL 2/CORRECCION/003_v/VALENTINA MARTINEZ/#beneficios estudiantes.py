"""
#ejercicio 1

promedio = float(input("indique su promedio final (ejemplo 4.2):   "))
condicion = int(input("indique su condicion socioeconomicas (1-10)"))



beneficio1 = 0.25
beneficio2 = 0.18
beneficio3 = 0.15
beneficio4 = 0.12
adicional = 0.05
arancel =2200000
matricula=95000
suma= (arancel + matricula)

if promedio >6.5 and condicion <=2:
    pago = (suma * beneficio1)
    print(f"el total a pagas es: {pago} ")
    if promedio >= 6.0 and condicion<= 3:
        desc_extra= (pago * beneficio4)
        print(f"total a pagar con descuentos integrados es: {desc_extra} ")

else:
    promedio >6.5 and condicion (3 or 4)
    pago = (suma * beneficio2)
    print(f"el total a pagas es: {pago} ")
    if promedio >= 6.0 and condicion<= 3:
        desc_extra= (pago * beneficio4)
        print(f"total a pagar con descuentos integrados es: {desc_extra} ")


if promedio >5.5 and promedio>=6.5 and condicion >=2:
    pago = (suma * beneficio3)
    print(f"el total a pagas es: {pago} ")
    if promedio >= 6.0 and condicion<= 3:
        desc_extra= (pago * beneficio4)
        print(f"total a pagar con descuentos integrados es: {desc_extra} ")

if promedio >5.5 or promedio>=6.5 and condicion (3 or 4):
    pago = (suma * beneficio4)
    print(f"el total a pagas es: {pago} ")
    if promedio >= 6.0 and condicion<= 3:
        desc_extra= (pago * beneficio4)
        print(f"total a pagar con descuentos integrados es: {desc_extra} ")
else:
    promedio <5.5 and condicion <4
    pago = suma
    print(f"el total a pagas es: {pago} ")


"""
#ejercicio 2 

import random
num1 = int(input("indique un numero  "))

num2 = int(input("indique un numero mayor al primero "))

suma = (num1 + num2)
resta= (num1-num2)

intentos=0


if num1>= num2:
    print("error ingrese un numero menor al primer valor ")
else:
    puntomedio = (suma) / 2
    ajuste = 0.2
    puntomedio1= (puntomedio* ajuste)

    numsectreto = float(puntomedio1 + random )


if intentos ==1:
    print("adivina el numero  ")
    if intentos == numsectreto:
        print("felicitaciones, adivinaste la respuesta")
    else:
        print("intentalo nuevamente    ")
    
if intentos == 2:
 if intentos == numsectreto:
        print("felicitaciones, adivinaste la respuesta")
 else:
     print("intentalo nuevamente    ")
     if intentos < numsectreto:
         print("pista: el numero secreto es mayor que su primer intento")
     else:
         intentos >numsectreto
         print ("pista: el numero secreto es menor que su primer intento")
    
        
if intentos ==3:
    print (f"perdiste el numero correcto era: {numsectreto}")



