
arancel = 2200000
matricula = 95000

promedio = float(input("Ingrese el promedio: "))
decil = int(input("Ingrese el decil: "))

# Descuento en arancel
descuento_arancel = 0.0

if promedio >= 6.5:
    if 1<= decil <= 2:
        descuento_arancel = 0.25
    elif 3 <= decil <= 4:
        descuento_arancel = 0.18
elif 5.5 < promedio <= 6.5:
    if 1<= decil <= 2:
        descuento_arancel = 0.15
    elif 3 <= decil <= 4:
        descuento_arancel = 0.12


descuento_matricula = 0.0
if decil >= 1 and decil <= 3:
    descuento_matricula = 0.12
if promedio >= 6.0:
        descuento_matricula += 0.05


arancel_final = arancel * (1 - descuento_arancel)
matricula_final = matricula * (1 - descuento_matricula)

print(f"Arancel final: ${arancel_final}")
print(f"Matrícula final: ${matricula_final}")
