

arancel = 2200000
matricula = 95000

promedio = float(input("Ingrese promedio: "))
decil = int(input("Ingrese decil: "))
arancel_final = 0
descuento_matricula = 0
matricula_final = 0
descuento = 0
descuento5 = 0
descuento_prom = 0
matricula2_final = 0

if promedio > 6.5:
    if decil == 1 or decil == 2:
        descuento = arancel * 0.25
        descuento_matricula = matricula * 0.17 # le sume el 5%
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
    elif decil == 3:
        descuento = arancel * 0.18
        descuento_matricula = matricula * 0.17 # le sume el 5%
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
    elif decil == 4:
        descuento = arancel * 0.12
        descuento_matricula = matricula * 0.05 
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
if 5.5 < promedio <= 6.5:
    if decil == 1 or decil == 2:
        descuento = arancel * 0.15
        descuento_matricula = matricula * 0.12
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
        if promedio >= 6.0:
            descuento5 = matricula_final * 0.05
            matricula_final = matricula_final - descuento5
    elif decil == 3:
        descuento = arancel * 0.12
        descuento_matricula = matricula * 0.12
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
        if promedio >= 6.0:
            descuento5 = matricula_final * 0.05
            matricula_final = matricula_final - descuento5
    elif decil == 4:
        descuento = arancel * 0.12
        arancel_final = arancel - descuento
        matricula_final = matricula - descuento_matricula
        if promedio >= 6.0:
            descuento5 = matricula_final * 0.05
            matricula_final = matricula_final - descuento5
else:
    arancel_final = arancel - descuento
    matricula_final = matricula - descuento_matricula


print(arancel_final)
print(matricula_final)

    



