ARANCEL = 2200000
MATRICULA = 95000

promedio = float(input("Ingrese su promedio final con el que salio del colegio: "))
decil = (input("Ingrese el decil al que pertenece su grupo familiar (entre 1 y 10): "))




if promedio > 6.5:
    if decil == "1" or "2":
        beneficio = ARANCEL *(1- 0.25)
    elif decil == "3" or "4":
        beneficio = ARANCEL *(1- 0.18)
elif 5.5 < promedio <= 6.5:
    if decil == "1" or "2":
        beneficio = ARANCEL *(1 - 0.15)
    elif decil == "3" or "4":
        beneficio = ARANCEL *(1- 0.12)
else:
    beneficio = ARANCEL
print(f"El valor del arancel es: {beneficio}.")

if decil == "5":
    print (f"El valor de la matricula es: {MATRICULA}")
elif decil == "1" or "2" or "3":
    if promedio >= 6.0:
        beneficio2= MATRICULA *(1- 0.17)
        print(f"El valor de la matricula es: {beneficio2}")
    else:
        beneficio2 = MATRICULA * (1- 0.12)
        print(f"El valor de la matricula es: {beneficio2}.")

