#mensualidad
arancel = 2200000
matricula = 95000
descuento_arancel = 0
descuento_matricula = 0

promedio = float(input("ingrese promedio (ej: 6.0): "))
decil = int(input("ingrese el decil (entre 1-10):"))

#descuento arancel
if promedio > 6.5 :
    if decil == 1 or 2 :
        descuento_arancel = 0.25
    elif decil == 3 or 4 : 
        descuento_arancel = 0.18
    else: 
        print("ingrese decil valido")
elif 5.5 < promedio <= 6.5 :
    if decil == 1 or 2 :
        descuento_arancel = 0.15
    elif decil == 3 or 4: 
        descuento_arancel = 0.12
    else: 
        print("ingrese decil valido")
else: 
    print("No cuenta con descuento por promedio bajo")

#descuento matricula
if decil <= 3:
    descuento_matricula = 0.12
    if promedio >= 6.0 :
        descuento_matricula += 0.05

print(f"El valor del arancel es: {arancel * (1 - descuento_arancel)}")
print(f"El valor de la matricula es: {matricula * (1 - descuento_matricula)}")