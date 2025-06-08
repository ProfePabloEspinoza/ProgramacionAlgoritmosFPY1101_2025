
condicion_academica = float(input("¿Cuál es su condición académica? (ej. 4.5): "))
condicion_socioeconomica = int(input("¿Cuál es su condición socioeconómica? (DECIL 1-10): "))
arancel_base = 2200000
matricula_base = 95000
beneficio_arancel = 0
beneficio_matricula = 0

if condicion_academica > 6.5:
    if condicion_socioeconomica in [1, 2]:
        beneficio_arancel = 0.25  
    elif condicion_socioeconomica in [3, 4]:
        beneficio_arancel = 0.18  
elif 5.5 < condicion_academica <= 6.5:
    if condicion_socioeconomica in [1, 2]:
        beneficio_arancel = 0.15 
    elif condicion_socioeconomica in [3, 4]:
        beneficio_arancel = 0.12

if condicion_socioeconomica in [1, 2, 3]:
    beneficio_matricula = 0.12  
    if condicion_academica >= 6.0:
        beneficio_matricula += 0.05


monto_arancel = arancel_base * (1 - beneficio_arancel)
monto_matricula = matricula_base * (1 - beneficio_matricula)

print(f"Descuento en arancel: {beneficio_arancel * 100:.0f}%")
print(f"Monto final a pagar por arancel: ${monto_arancel:,.0f}")
print(f"Descuento en matrícula: {beneficio_matricula * 100:.0f}%")
print(f"Monto final a pagar por matrícula: ${monto_matricula:,.0f}")