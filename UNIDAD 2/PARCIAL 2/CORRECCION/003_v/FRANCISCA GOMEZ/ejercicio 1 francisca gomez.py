
# Valores base
arancel_base = 2200000
matricula_base = 95000
#datos
promedio = float(input("Ingresa tu promedio: "))
decil = int(input("Ingresa el decil (1-10): "))

# Inicializar descuentos
descuento_arancel = 0
descuento_matricula = 0

# descuento en arancel
if promedio > 6.5:
    if 1 <= decil <= 2:
        descuento_arancel = 0.25
    elif 3 <= decil <= 4:
        descuento_arancel = 0.18
elif 5.5 < promedio <= 6.5:
    if 1 <= decil <= 2:
        descuento_arancel = 0.15
    elif 3 <= decil <= 4:
        descuento_arancel = 0.12

# descuentos en matrícula
if decil in [1, 2, 3]:
    descuento_matricula = 0.12
    if promedio >= 6.0:
        descuento_matricula += 0.05

# Calcular costos finales
arancel_final = arancel_base * (1 - descuento_arancel)
matricula_final = matricula_base * (1 - descuento_matricula)

# Mostrar resultados
print(f"El arancel final es: ${arancel_final:,.2f}")
print(f"La matrícula final es: ${matricula_final:,.2f}")

