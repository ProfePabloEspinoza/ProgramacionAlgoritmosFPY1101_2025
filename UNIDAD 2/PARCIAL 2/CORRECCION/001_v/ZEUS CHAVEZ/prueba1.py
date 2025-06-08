condicion1 = float(input("Ingrese su Promedio del Colegio o liceo"))
socio = int(input("Ingrese su Condicion Socio Economico"))

ARANCEL = 2200000
MATRICULA= 95000
extra = MATRICULA * 0.12
extra2 = MATRICULA * 0.05

if 6.5 < condicion1 <= 7.0 and 1 <= socio <= 2:
    bono = (ARANCEL-(ARANCEL * 0.25))
    print("Tu descuento del Arancel es:", bono)
elif 6.5 < condicion1 <= 7.0 and 3 <= socio <= 4:
    bono = (ARANCEL-(ARANCEL * 0.18))
    print("Tu descuento del Arancel es:", bono)
    print("Tu arancel es", MATRICULA)
elif 5.5 <= condicion1 <= 6.5 and 1 <= socio <= 2:
    bono = (ARANCEL-(ARANCEL * 0.15))
    print("Tu descuento del Arancel es:", bono)
    print("Tu arancel es", MATRICULA)
elif 5.5 <= condicion1 <= 6.5 and 3 <= socio <= 4:
    bono = (ARANCEL-(ARANCEL * 0.12))
    print("Tu descuento del Arancel es:", bono)
    print("Tu arancel es", MATRICULA)
elif 4.5 <= condicion1 <= 7.0 and socio == 5:
    print("Tu arancel es", ARANCEL)
    print("Tu arancel es", MATRICULA)
if 6.0 <= condicion1 <= 7.0 and 1 <= socio <= 3:
    bono = ((MATRICULA - extra) - extra2)
    print("Valor de la matricula es:", bono)
