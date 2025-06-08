"""""
# Constantes

ARANCEL = 2200000
MATRICULA = 95000

def obtener_descuento_arancel(promedio, decil):
    if promedio > 6.5:
        if decil in [1, 2]:
            return 0.25
        elif decil in [3, 4]:
            return 0.18
    elif 5.5 < promedio <= 6.5:
        if decil in [1, 2]:
            return 0.15
        elif decil in [3, 4]:
            return 0.12
    return 0.0

def obtener_descuento_matricula(promedio, decil):
    descuento = 0.0
    if decil in [1, 2, 3]:
        descuento += 0.12
        if promedio >= 6.0:
            descuento += 0.05
    return descuento

def calcular_valores_finales(promedio, decil):
    descuento_arancel = obtener_descuento_arancel(promedio, decil)
    descuento_matricula = obtener_descuento_matricula(promedio, decil)

    arancel_final = ARANCEL * (1 - descuento_arancel)
    matricula_final = MATRICULA * (1 - descuento_matricula)

    return arancel_final, matricula_final, descuento_arancel, descuento_matricula

def mostrar_resultado(arancel_final, matricula_final, desc_arancel, desc_matricula):
    print("\n--- Resultados ---")
    print(f"Descuento aplicado al arancel: {desc_arancel*100:.0f}%")
    print(f"Valor final del arancel: ${arancel_final:,.0f}")
    print(f"Descuento aplicado a la matrícula: {desc_matricula*100:.0f}%")
    print(f"Valor final de la matrícula: ${matricula_final:,.0f}")

# Programa principal
try:
    promedio = float(input("Ingrese el promedio final (1.0 a 7.0): "))
    decil = int(input("Ingrese el decil socioeconómico (1 a 10): "))

    if not (1 <= decil <= 10 and 1.0 <= promedio <= 7.0):
        print("Error: Ingrese valores válidos.")
    else:
        arancel, matricula, desc_ar, desc_mat = calcular_valores_finales(promedio, decil)
        mostrar_resultado(arancel, matricula, desc_ar, desc_mat)

except ValueError:
    print("Error: Ingrese datos numéricos correctamente.")
"""
"""""
import random

# Paso 1: Solicitar un rango válido
while True:
    try:
        num1 = int(input("Ingrese el primer número : "))
        num2 = int(input("Ingrese el segundo número : "))

        if num1 < num2:
            break
        else:
            print("El primer número debe ser menor que el segundo. Intenta nuevamente.")
    except ValueError:
        print("Por favor, ingresa solo números enteros.")

# Paso 2: Calcular el punto medio y ajuste
punto_medio = (num1 + num2) / 2
ajuste = (num2 - num1) * 0.2

# Paso 3: Generar número aleatorio cerca del punto medio
numero_secreto = random.uniform(punto_medio - ajuste, punto_medio + ajuste)
numero_secreto = round(numero_secreto)

# Paso 4: Juego con 3 intentos
intentos = []
ganaste = False

print("\n¡Intenta adivinar el número secreto! Tienes 3 intentos.")

for intento in range(1, 4):
    try:
        adivinanza = int(input(f"Intento {intento}: "))
        intentos.append(adivinanza)

        if adivinanza == numero_secreto:
            print(" ¡Felicitaciones, pudiste adivinar!")
            ganaste = True
            break
        elif adivinanza < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")

        # En el segundo intento, dar pista sobre cuál fue más cercano
        if intento == 2:
            distancia1 = abs(intentos[0] - numero_secreto)
            distancia2 = abs(intentos[1] - numero_secreto)
            if distancia1 < distancia2:
                print("Pista: Tu primer intento estuvo más cerca.")
            elif distancia2 < distancia1:
                print("Pista: Tu segundo intento estuvo más cerca.")
            else:
                print("Pista: Ambos intentos estuvieron igual de cerca.")

    except ValueError:
        print("Por favor, ingresa un número entero válido.")
"""