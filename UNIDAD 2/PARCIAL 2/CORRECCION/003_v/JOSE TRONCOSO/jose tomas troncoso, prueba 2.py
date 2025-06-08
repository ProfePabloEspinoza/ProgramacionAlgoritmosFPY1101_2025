# ejeercicio 1

promedio = float(input("ingrese promedio"))
decil = int(input("ingrese decil"))

arancel = 2200000
matricula = 95000


if promedio > 6.5 and decil <= 2:
    arancel = arancel - (arancel * 0.25)
elif promedio > 6.5 and decil <= 4:
    arancel = arancel - (arancel * 0.18)
elif promedio >= 5.5 and decil <= 2:
    arancel = arancel - (arancel * 0.15)
elif promedio >= 5.5 and decil <= 4:
    arancel = arancel - (arancel * 0.12)
else:
    arancel = arancel  


if decil <= 3 and promedio >= 6.0:
    matricula = matricula - (matricula * 0.12) - (matricula * 0.05)
elif decil <= 3:
    matricula = matricula - (matricula * 0.12)
else:
    matricula = matricula  
    
print(f"el valor del arancel es: ${arancel}")
print(f"el valor de la matrícula es: ${matricula}")

"""

# ejercicio 2

import random

num1 = int(input("ingrese el primer número : "))
num2 = int(input("ingrese el segundo número que sea mayor al primero: "))

if num1 < num2:
    punto_medio = (num1 + num2) / 2
    ajuste = (num2 - num1) * 0.2

    minimo = int(punto_medio - ajuste)
    maximo = int(punto_medio + ajuste)
    secreto = random.randint(minimo, maximo)
    secreto = random.randint(num1 + 1, num2 - 1)

   
    for intento in range(1, 4):
        adivina = int(input(f"Intento {intento}: "))
        
        if adivina == secreto:
            print("feliciadades, adivinaste el numero")
            break
        elif adivina < secreto:
            print("el numero es mayor.")
        else:
            print("el numero es menor.")
        
        if intento == 3:
            print("perdiste. el numero era:", secreto)
else:
    print(" el primer número debe ser menor que el segundo.")
    
"""