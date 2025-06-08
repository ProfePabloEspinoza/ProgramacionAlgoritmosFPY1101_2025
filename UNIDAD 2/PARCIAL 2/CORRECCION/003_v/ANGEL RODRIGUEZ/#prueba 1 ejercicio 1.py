#prueba 1 ejercicio 1
#beneficios y descuentos estudiantiles
print ("ingresar datos del estudiante")
academico = float(input("ingrese su promedio academico: "))
decil = int(input("decil de su grupo familiar(1/10): "))

arancel_base = 2200000
matricula_base = 95000



if academico >=6.5:
    if decil == 1 or decil ==2:
        descuento_aracel = 0.25
    elif decil == 3 or decil == 4:
        descuento_aracel = 0.18
elif 5.5 <= academico <= 6.5:
    if decil == 1 or decil ==2:
        descuento_aracel = 0.15
    elif decil == 3 or decil == 4:
        descuento_aracel = 0.12

descuento_matricula = 0

if decil == 1 or decil == 2 or decil == 3:
    descuento_matricula = 0.12  
    if academico >= 6.0:
        descuento_matricula += 0.05  

    arancel_final = arancel_base * (1-descuento_aracel)
    matricula_final = matricula_base * (1-descuento_matricula)

print("beneficios y descuentos aplicados: ")
print("descuento en arancel: ", descuento_aracel)
print("descuento en matricula: ", descuento_matricula)
print("arancel final: ", arancel_final)
print("matricula final: ", matricula_final)
print("total a pagar: ", arancel_final + matricula_final)

#fin



#ejercicio 2
# Juego de adivinanza de números
import random

num1 = int(input("Ingrese el primer número (menor): "))
num2 = int(input("Ingrese el segundo número (mayor): "))

if num1 < num2:
    numero_secreto = random.randint(num1, num2)

    intento1 = int(input(f"Intento 1: Ingresa un número entre {num1} y {num2}: "))
    if intento1 == numero_secreto:
        print("¡Felicitaciones, adivinaste el número!")
    else:
        intento2 = int(input(f"Intento 2: Ingresa un número entre {num1} y {num2}: "))
        if intento2 == numero_secreto:
            print("¡Felicitaciones, adivinaste el número!")
        else:
            intento3 = int(input(f"Intento 3: Ingresa un número entre {num1} y {num2}: "))
            if intento3 == numero_secreto:
                print("¡Felicitaciones, adivinaste el número!")
            else:
                print(f"Perdiste. El número correcto era {numero_secreto}.")
else:
    print("El primer número debe ser menor que el segundo.")
#fin
