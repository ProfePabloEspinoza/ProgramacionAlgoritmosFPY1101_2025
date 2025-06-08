# --- Configuración Interna (Contexto del Ejercicio 1) ---
arancel_base = 2200000.0

# Perfil secreto del estudiante (para calcular el valor a adivinar)
promedio_secreto = 6.1
decil_secreto = 2

# Calcular el descuento real basado en el perfil secreto
descuento_real_A = 0.0 # Descuento Arancel

if promedio_secreto > 6.5 and (decil_secreto == 1 or decil_secreto == 2):
    descuento_real_A = 0.25
elif promedio_secreto > 6.5 and (decil_secreto == 3 or decil_secreto == 4):
    descuento_real_A = 0.18
elif (promedio_secreto > 5.5 and promedio_secreto <= 6.5) and (decil_secreto == 1 or decil_secreto == 2):
    # Este es el caso para promedio 6.1 y decil 2
    descuento_real_A = 0.15
elif (promedio_secreto > 5.5 and promedio_secreto <= 6.5) and (decil_secreto == 3 or decil_secreto == 4):
    descuento_real_A = 0.12
# else: No hay descuento si no cumple las condiciones anteriores (descuento_real_A sigue siendo 0.0)

# Calcular el arancel final real (el valor a adivinar)
arancel_final_real = arancel_base * (1 - descuento_real_A)

# --- Inicio del Juego (Interfaz con el usuario) ---
print(f"El arancel base es ${arancel_base:.0f}. Se aplican descuentos por rendimiento y decil.")
print("¡Intenta adivinar el monto final del arancel!")

ganado = False # Variable para controlar si ya se ganó

# --- Intento 1 ---
# Usamos float para permitir decimales, aunque los ejemplos sean enteros
intento1 = float(input('\nIntento 1: Ingrese el monto: '))

if intento1 == arancel_final_real:
    print("¡Felicitaciones! Adivinaste el monto exacto en el intento 1.")
    ganado = True
else:
    # Dar pista de mayor/menor para intento 1
    if arancel_final_real > intento1:
        print("El arancel final real es MAYOR.")
    else: # arancel_final_real < intento1
        print("El arancel final real es MENOR.")

    # --- Intento 2 (Solo si no ganó en el intento 1) ---
    if not ganado: # Es lo mismo que if ganado == False:
        intento2 = float(input('\nIntento 2: Ingrese el monto: '))

        if intento2 == arancel_final_real:
            print("¡Felicitaciones! Adivinaste el monto exacto en el intento 2.")
            ganado = True
        else:
            # Dar pista de mayor/menor para intento 2
            if arancel_final_real > intento2:
                print("El arancel final real es MAYOR.")
            else: # arancel_final_real < intento2
                print("El arancel final real es MENOR.")

            # Calcular distancias absolutas para la pista de cercanía
            distancia1 = abs(arancel_final_real - intento1)
            distancia2 = abs(arancel_final_real - intento2)

            # Dar pista de cercanía
            print("Pista:", end=" ")
            if distancia1 < distancia2:
                # Usamos :.0f para mostrar los montos sin decimales en la pista
                print(f"El monto real está más cerca de {intento1:.0f} que de {intento2:.0f}.")
            elif distancia2 < distancia1:
                print(f"El monto real está más cerca de {intento2:.0f} que de {intento1:.0f}.")
            else: # distancias iguales
                print(f"El monto real está a la misma distancia de {intento1:.0f} que de {intento2:.0f}.")

            # --- Intento 3 (Solo si no ganó en el intento 2) ---
            if not ganado:
                intento3 = float(input('\nIntento 3: Ingrese el monto: '))

                if intento3 == arancel_final_real:
                    print("¡Felicitaciones! Adivinaste el monto exacto en el intento 3.")
                    ganado = True
                else:
                    # Si llega aquí y no acierta, pierde.
                    # Mostramos el arancel real formateado
                    print(f"\nPerdiste. El arancel final real era: {arancel_final_real:.0f}")

# Nota: El código usa :.0f en algunos prints para mostrar los montos de arancel como enteros,
#       lo cual es común al hablar de dinero, aunque internamente se manejen como float.