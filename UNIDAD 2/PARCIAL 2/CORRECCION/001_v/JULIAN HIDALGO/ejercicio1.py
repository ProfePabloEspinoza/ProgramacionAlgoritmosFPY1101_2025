promedio = float(input('Ingrese su promedio: ')) 
decil =  float(input('Ingrese el decil (1-10): '))
desc_arancel = 1
desc_matricula = 1
arancel = 2200000
matricula = 95000

if promedio > 6.5:
        if decil == 1 or decil == 2:
            desc_arancel = 0.75
        elif decil == 3 or decil == 4:
            desc_arancel = 0.82
elif 5.5 < promedio <= 6.5:
        if decil == 1 or decil == 2:
            desc_arancel = 0.85
        elif decil == 3 or decil == 4:
            desc_arancel = 0.88

if 1 <= decil <= 3:
    desc_matricula = 0.88
    if promedio >= 6.0:
        desc_matricula = 0.83

aran_final = arancel * desc_arancel
matri_final = matricula * desc_matricula

print(f'El valor del arancer es: {int(aran_final)}\nEl valor de la matricula es: {int(matri_final)} ')

