promedio = float(input('Ingrese su promedio: '))
decil = int(input('Ingrese el decil (1-10): '))
descuento_A = 0
descuento_M = 0

# Definir descuentos según promedio y decil
if promedio > 6.5 and (decil == 1 or decil == 2):
    descuento_A = 0.25
elif promedio > 6.5 and (decil == 3 or decil == 4):
    descuento_A = 0.18
elif (promedio > 5.5 and promedio <= 6.5) and (decil == 1 or decil == 2):
    descuento_A = 0.15
elif (promedio > 5.5 and promedio <= 6.5) and (decil == 3 or decil == 4):
    descuento_A = 0.12

# Descuento en matrícula según decil
if decil == 1 or decil == 2 or decil == 3:
    descuento_M = 0.12
    if promedio >= 6.0:
        descuento_M = 0.17  # Se suma el 5% adicional

# Calcular valores finales
arancel_base = 2200000
matricula_base = 95000
arancel = arancel_base - (arancel_base * descuento_A)
matricula = matricula_base - (matricula_base * descuento_M)

# Mostrar resultados
print('El valor del arancel es:', round(arancel))
print('El valor de la matrícula es:', round(matricula))
