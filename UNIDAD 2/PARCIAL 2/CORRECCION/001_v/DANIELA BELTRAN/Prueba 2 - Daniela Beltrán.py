
c_academicas = float(input("Ingrese su promedio: "))
c_socioeconomicas = int(input("Ingrese el decil:(1-10): "))
arancel = 2200000
matricula = 95000

if c_academicas > 6.5 and c_socioeconomicas in (1, 2):
   descuento_arancel = arancel * (1 - 0.25)
elif c_academicas > 6.5 and c_socioeconomicas in (3, 4):
    descuento_arancel = arancel * (1- 0.18)
elif c_academicas < 5.5 and c_academicas <= 6.5 and c_socioeconomicas in (1, 2):
    descuento_arancel = arancel * (1 - 0.15)
elif c_academicas < 5.5 and c_academicas <= 6.5 and c_socioeconomicas in (3, 4):
    descuento_arancel = arancel * (1- 0.12)

if c_socioeconomicas in (1, 2, 3):
    descuento_matricula = matricula * (1- 0.12)
elif c_academicas >= 6.0 and c_socioeconomicas in (1, 2, 3):
   descuento_matricula = matricula * (-1 - 0.05)

print(f"El valor del arancel es: ${descuento_arancel: .2f} ")
print(f"El valor de la matricula es: ${descuento_matricula: .2f}")
