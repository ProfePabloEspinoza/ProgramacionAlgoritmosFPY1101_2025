arancel_base = 2200000
matricula_base = 95000

print("Bienvenido al sistema de cálculo de aranceles y matrículas")
print("Por favor, ingrese los siguientes datos para calcular su arancel y matrícula:")
promedio = float(input("Ingrese su promedio: "))
decil = int(input("Ingrese el decil (1-10): "))


if promedio > 6.5 and decil in [1, 2]:
    descuento_arancel = 0.25  # Se aplica un 25% de descuento
elif promedio > 6.5 and decil in [3, 4]:
    descuento_arancel = 0.18  # Se aplica un 18% de descuento
elif 5.5 < promedio <= 6.5 and decil in [1, 2]:
    descuento_arancel = 0.15  # Se aplica un 15% de descuento
elif 5.5 < promedio <= 6.5 and decil in [3, 4]:
    descuento_arancel = 0.12  # Se aplica un 12% de descuento
else:
    descuento_arancel = 0  # No se aplica descuento


if decil in (1, 2, 3):
    descuento_matricula = 0.12 # Se aplica un 12% de descuento
    if promedio >= 6.0:
        descuento_matricula += 0.05 # Se aplica un 5% adicional de descuento
else:
    descuento_matricula = 0 # No se aplica descuento

arancel_final = arancel_base * (1 - descuento_arancel)
matricula_final = matricula_base * (1 - descuento_matricula)


print(f"El valor del arancel es: ${arancel_final:,.0f}")
print(f"El valor de la matrícula es: ${matricula_final:,.0f}")
