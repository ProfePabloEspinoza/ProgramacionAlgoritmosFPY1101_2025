arancel = 2200000

matricula = 95000

promedio = int(input("Ingrese su ultimo promedio de colegio/liceo: "))

condicion_socioeconomica = int(input("Ingrese su decil (1-10): "))

if promedio > 6.5 and (condicion_socioeconomica == 1 or condicion_socioeconomica == 2):
    decuento_arancel = 0.25
elif promedio > 6.5 and (condicion_socioeconomica == 3 or condicion_socioeconomica == 4 ):
    decuento_arancel = 0.18  
elif promedio > 5.5 and promedio <= 6.5 and (condicion_socioeconomica == 1 or condicion_socioeconomica == 2):
    decuento_arancel = 0.15
elif promedio > 5.5 and promedio <= 6.5 and (condicion_socioeconomica == 3 or condicion_socioeconomica == 4):
    decuento_arancel = 0.12
else:
    decuento_arancel = 0.0    


decuento_matricula = 0.0 
if condicion_socioeconomica == 1 or condicion_socioeconomica == 2 or condicion_socioeconomica == 3:
    decuento_matricula = 0.12
    if promedio >= 6.0:
        decuento_matricula += 0.05

arancel_final = arancel - (arancel * decuento_arancel)
matricula_final = matricula - (matricula * decuento_matricula)

print(arancel_final)
print(matricula_final)