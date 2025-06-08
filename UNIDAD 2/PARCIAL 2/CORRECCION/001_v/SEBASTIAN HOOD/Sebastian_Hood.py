
estado_socio = int(input("ingrese el decil de su grupo familiar:(del 1 al 10) "))
estado_academico = float(input("imgrese su promedio de notas: "))
arancel_base = 2200000
matricula = 95000

	
if estado_socio in [1, 2] and estado_academico >= 6.5:
		descuento_base = 0.25
elif estado_socio in [3, 4] and estado_academico >= 6.5:
		descuento_base = 0.18
elif estado_socio in [1, 2] and 5.5 <= estado_academico <= 6.5:
		descuento_base = 0.15
elif estado_socio in [3, 4] and 5.5 <= estado_academico <= 6.5:
		descuento_base = 0.12
else:
		descuento_base = 0.0

	
if estado_socio in [1, 2, 3] and estado_academico >= 6.0:
		descuento_matricula = 0.17
elif estado_socio in [1, 2, 3]:
		descuento_matricula = 0.12
else:
		descuento_matricula = 0.0

arancel_final = arancel_base - (arancel_base * descuento_base)
matricula_final = matricula - (matricula * descuento_matricula)

print("su arancel es de: ", arancel_final)
print("su matricula es de: ", matricula_final)
