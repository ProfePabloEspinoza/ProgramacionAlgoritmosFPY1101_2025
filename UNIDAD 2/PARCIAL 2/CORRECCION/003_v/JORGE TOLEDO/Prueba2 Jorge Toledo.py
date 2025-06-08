print ("Bienvenidos al sistema de Beneficios")
print ("_"*40)

promedio = float(input("Ingrese su promedio 0.0/7.0: "))
decil = int(input("Ingrese su Decil 1/10: "))
arancel = 2200000
matricula = 95000
descuento_arancel = 0
descuento_matricula = 0

if promedio >= 6.5 and  1 <= decil <= 10: 
    if decil == 1 or decil == 2:
        descuento_arancel = 0.25
elif decil == 3 or decil == 4:
    descuento_arancel = 0.18
if 5.5 < promedio <= 6.5:
    if decil == 1 or decil == 2:
        descuento_arancel = 0.15
elif decil == 3 or decil == 4:
    descuento_arancel = 0.12

if decil == 1 or decil == 2 or decil == 3:
        descuento_matricula = 0.12
        if promedio >= 6.0:
            descuento_matricula += 0.05
else:
    print("Error: Promedio debe estar entre 0.0 y 7.0, y decil entre 1 y 10.")

arancel_final = arancel * (1 - descuento_arancel)
matricula_final = matricula * (1 - descuento_matricula)

print("El arancel inicial es: $2.200.000")
print("El valor de la matricula es: $95.00")
print(f"Su Arancel final es: ", arancel_final)
print(f"Su valor matricula es: ", matricula_final)