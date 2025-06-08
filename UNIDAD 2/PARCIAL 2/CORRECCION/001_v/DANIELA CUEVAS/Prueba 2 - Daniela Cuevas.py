#EJERCICIO 1

VALOR_BASE_ARANCEL = 2200000
VALOR_BASE_MATRICULA = 95000

#Solicitar datos 

Promedio_notas = float(input("Ingrese su promedio: "))
Decil = int(input("Ingrese su decil (1-10): "))

#Calcular beneficios

porcentaje_beneficio = 0

if Promedio_notas > 6.5 and Decil == 1 or Decil == 2:
   porcentaje_beneficio = 0.25
elif Promedio_notas > 6.5 and Decil == 3 or Decil == 4:
   porcentaje_beneficio = 0.18
elif Promedio_notas > 5.5 and Decil == 1 or Decil == 2:
   porcentaje_beneficio = 0.15
elif Promedio_notas <= 6.5 and Decil == 1 or Decil == 2:
   porcentaje_beneficio = 0.15
elif Promedio_notas > 5.5 and Decil == 3 or Decil == 4:
   porcentaje_beneficio = 0.12
elif Promedio_notas <= 6.5 and Decil == 3 or Decil == 4:
   porcentaje_beneficio = 0.12
else:
   print("No aplica beneficio a su decil")
   porcentaje_beneficio = 0.0

valor_beneficio_arancel = VALOR_BASE_ARANCEL - (VALOR_BASE_ARANCEL * porcentaje_beneficio)

if Decil == 1 or 2 or 3:
   descuento_matricula = 0.12
if Promedio_notas >= 6.0 and Decil == 1 or Decil ==2 or Decil ==3:
   descuento_matricula_adicional = 0.05

Valor_beneficio_matricula = VALOR_BASE_MATRICULA - (VALOR_BASE_MATRICULA * (descuento_matricula + descuento_matricula_adicional)) 

#Mostrar resultado

print(f"El valor del arancel es: {valor_beneficio_arancel}")
print(f"El valor de la matrícula es: {Valor_beneficio_matricula}")




#EJERCICIO 2

import random
print("Juego de adivinanza")
print("Ingresa dos números para establecer un rango")

#Solicitar numeros
num1 = int(input("Ingrese límite inferior: "))
num2 = int(input("Ingrese límite superior: "))

#Verificar numeros 
if num1 >= num2:
    print("Error, el primer número debe ser menor al número 2")
else:
    punto_medio = (num1+num2)/3
    ajuste =(num1-num2)*0.2
    signo_a = 1 if random.random() > 0.5 else -1
    numero_adivinanza = int(punto_medio + (signo_a*random.random()*ajuste))
    if numero_adivinanza < num1:
        numero_adivinanza = num1
    if numero_adivinanza > num2:
        numero_adivinanza = num2
    print(f"¡Adivina el número que genere entre {num1} y {num2}!")
    intento1 = int(input("intento 1: "))
    if intento1 == numero_adivinanza:
        print("Felicitaciones,pudiste adivinar")
    else:
        if intento1 > numero_adivinanza:
            print("el número es mayor")
        else:
            print("el número es menor")
        intento2 = int(input("intento 2: "))
        if intento2 == numero_adivinanza:
            print("Felicitaciones,pudiste adivinar")
        else:
            if intento2 > numero_adivinanza:
                print("el número es mayor")
            else:
                print("el número es menor")
            diferencia1 = numero_adivinanza - intento1
            diferencia2 = numero_adivinanza - intento2
            if diferencia1 < diferencia2:
                print(f"Intento número 1. Pista: {intento1} está mas cerca del número que buscas")
            elif diferencia1 > diferencia2:
                print(f"Intento número 2. Pista: {intento2} está mas cerca del número que buscas")
            else:
                print("Pista: los dos intentos estuvieron igual de cerca del número que buscas")
                intento3 = int(input("intento 3: "))
                if intento1 == numero_adivinanza:
                    print("Felicitaciones,pudiste adivinar")
                else:
                    print(f"Perdiste, el número era: {numero_adivinanza}")




